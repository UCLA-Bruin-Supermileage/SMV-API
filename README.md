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
### Bare Metal
- **NOTE**: 3.13 > Python version >= 3.10 is required, and libpq-dev is required (or Windows PostgreSQL equivalent)
- Create and activate a virtual environment, virtualenv env && source env/bin/activate
- Install requirements, pip install -r requirements.txt
### Docker File
-  docker build -t django-apache .
-  docker run -p 443:443 -p 80:80 -d django-apache
