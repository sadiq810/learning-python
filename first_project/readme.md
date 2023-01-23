## To create a project
- django-admin startproject mysite

## To run the project
- python manage.py runserver

## To create a pluggable app (djengo project)
- python manage.py startapp first_app
``then you have to tell about this app to djengo, goto settings.py file in your project and add entry to INSTALLED_APPS array``
  
## to create another route file per app you installed, 
- just create urls.py file in the app directory.
- and make an entry in the project urls file like
``
  from django.urls import include
  
    #and put below entry in urlpatterns
  path('contact/', include('first_app.urls')),
  ``
  
## adding templates folder in root and populate the path in settings.py 
``TEMPLATE_DIR = Path.joinpath(BASE_DIR, 'templates')``
- and put this variable in DIR key array in TEMPLATES array in settings.py

## static file support, add folder in the root directory and populate path in settings.py
``STATIC_DIR = Path.joinpath(BASE_DIR, 'static')``
- and add variable in settings.py
``STATICFILES_DIRS = [STATIC_DIR,]``
  - then add below line at the top of html page
    ``{% load static %}``
    - you can load images, css, js like below
    `` <img src="{% static 'images/image.jpg' %}" alt="">``