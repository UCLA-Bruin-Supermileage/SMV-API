# Use an official Ubuntu base image
FROM ubuntu:22.04

# Set environment variables to prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt update && apt install -y \
    apache2 \
    libapache2-mod-wsgi-py3 \
    python3 \
    python3-pip \
    python3-venv \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /var/www/SMV-API

# Copy Django project files
COPY . /var/www/SMV-API

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Collect static files and migrate
RUN python3 manage.py collectstatic --noinput

# Set correct permissions
RUN chown -R www-data:www-data /var/www/SMV-API

# Copy and enable Apache configuration
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
RUN a2enmod wsgi

# Enable SSL module and create a self-signed certificate
RUN a2enmod ssl \
    && mkdir -p /etc/apache2/ssl \
    && openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
       -keyout /etc/apache2/ssl/apache-selfsigned.key \
       -out /etc/apache2/ssl/apache-selfsigned.crt \
       -subj "/C=US/ST=CA/L=LA/O=UCLA/OU=SMV/CN=localhost"

# Expose port 80 for Apache
EXPOSE 80
EXPOSE 443

# Start Apache
CMD ["apache2ctl", "-D", "FOREGROUND"]
