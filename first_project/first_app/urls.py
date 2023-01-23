from django.urls import path
from first_app import views


urlpatterns = [
    path('', views.contact, name="contact"),
    path('one', views.contactOne, name="contact.one"),
    path('two', views.contactTwo, name="contact.two"),
]