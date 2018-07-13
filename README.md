GeoLocation:
eolocation is the process of converting addresses (like "1600 Amphitheatre Parkway, Mountain View, CA") into geographic coordinates (like latitude 37.423021 and longitude -122.083739).

Basic Django app is used to get data from the front end.
Tech:
1) Python 2.7
2) Django 1.10

Installation:
1) First clone the project, open your terminal and enter the command:
  >git clone https://github.com/Punith93/geolocation.git
  
2) Now create a virtual environment:
  >virtualenv geo
  
3) Now activate the virtual environment:
  >source geo/bin/activate
  
4) Now enter into the project folder:
  >cd geolocation
 
5) Now install the requirements:
  >pip install -r requirements.txt
  
6) Make Migrations:
  >python manage.py makemigrations
  
7) Make Migrate:
  >python manage.py migrate
  
8) runserver:
  >python manage.py runserver
  
