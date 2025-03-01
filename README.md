# Supermileage API 
The Django API behind the React dashboard frontend. This site receives MQTT data from the Data AcQuisition board on our Hydrogen powered car and stores it to a PostgreSQL database
## Components
### Django Admin
Accessible via /admin, this allows direct access to the database
### API Documentation
Accessible via /apidocs/schema/swagger-ui, this provides information on all accessible endpoints and their usage
### API Endpoints
Covered in depth in the documentation site and has root URL /api
## Server Components
- Requires PostgreSQL as backend, and can set in smvDashboard/settings.py
- Requires an MQTT server, set with the ip_address variable in smvDashboard/settings.py
## Build Instructions
- Please set DEBUG=False in smvDashboard/settings.py before deploying to production
- Please add secrets to .env file (contact SMV DAQ lead for access if required)
### Bare Metal (optimized for Ubuntu 22.04 LTS)
- **NOTE**: 3.13 > Python version > 3.10 is required, and libpq-dev is required (or Windows PostgreSQL equivalent)
	- `apt get libpq-dev`
1. Create and activate a virtual environment, `virtualenv env && source env/bin/activate`
2. Install requirements, `pip install -r requirements.txt`
3. Collect static files, `python manage.py collectstatic`
4. Check DEBUG flag
5. If any changes have been made to the database file, mqtt/models.py, make migrations and apply them to production database with `python manage.py makemigrations && python manage.py migrate`
6. Run server with `python manage.py runserver`
### Server Deployment Instructions
- Assuming Ubuntu 22.04 LTS VM with all prerequisites installed (apache2, libapache2-mod-wsgi-py3, python3, python3-pip, python3-venv, libpq-dev) and with Apache config file 000-default.conf located at /etc/apache2/sites-available/000-default.conf
1. Rename ~/SMV-API to ~/vX.XX
2. Clone SMV-API repository
3. Apply steps 2 through 5 from the bare metal steps above
4. Run: `sudo chmod 774 ~/SMV-API && sudo chown :www-data ~/SMV-API` (may need to adjust chmod to 777)
5. Restart Apache with `sudo systemctl restart apache2`
	-Error logs available at /var/log/apache2/error.log or on Sentry 
### Docker File
-  docker build -t django-apache .
-  docker run -p 443:443 -p 80:80 -d django-apache
