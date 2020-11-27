# Geolocation REST API

## Intro
<p>Simple API allowing storing geolocation data pulled from IPStack in database.</p>
<br>

## HTTP Methods
<p><b>GET </b></p>
<p>url: /geolocations/ </p>
<p>query param: <i>ip_or_url</i></p>
<br>

<p><b>POST </b></p>
<p>url: /geolocations/{pk}</p>
<br>
<p>url: /api/token/
<p>body params: username, password </p>
<br>

<p><b>DELETE </b></p>
<p>url: /geolocations/{pk}</p>
<br>

## Setup
1. Put your ipstack Your API Access Key to .env file
2. Run ```docker-compose up```
3. Run ```docker-compose run --rm web python3 manage.py migrate```
4. (optional) Create superuser using eg. ```docker-compose run --rm web python3 manage.py createsuperuser```
5. To add fake data to your database run ```docker-compose run --rm web python3 manage.py populate_database```

## Usage
<p>Play with API, create, remove, retrieve objects from database.</p>
<p>Remember to get your JWT token before sending a request!</p>

## Tests
To run tests use ```docker-compose run --rm web  pytest```
<br>
<br>

<p><i> *Disclaimer - this is just a demo version, so some of the functionalities are basic and simplifed (exceptions, factories) </i></p>
