Receives MQTT data from SMV on-board DAQ and stores it to a database. \
INSTALLATION: 
- site is in development.
- pip install -r requirements.txt
- python manage.py runserver \
Site Paths: 
- /dashboard: dashboard
- /dashboard/map: map display, in progress
- /admin: admin console
- /static: static files, served via Apache
- /ws: websocket, served via daphne \
[Notion Link](https://www.notion.so/matthewtsai/57c1ed5ef802477a9a5b9c2ce18886ef?v=d6d9acbf4d27457c8b4f7948b3179b13&pvs=4)

# Docker Instructions
- FOR PRODUCTION: Set DEBUG=False in smvDashboard/settings.py
- docker build -t django-apache .
- docker run -p 443:443 -p 80:80 -d django-apache

# API Documentation:
## /api

### /api/token
- supports POST
- {"username": "user", "password": "password"}
- returns access token and refresh token (JWT)

### /api/trip
- Supports POST, PUT, GET, PATCH, DELETE
- GET: 
  - no authentication required
  - lists all trips
- POST:
  - {"name": "TripName", "date_created": YYYY-MM-DD, "start": YYYY-MM-DD:HH:mm}
  - requires access token
  - add new trip
  - returns details of new trip, including ID
- GET /api/trip/<int:id>
  - get details of specified trip
- GET /api/trip/last
  - get details of latest trip