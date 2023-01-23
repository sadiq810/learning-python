from django.urls import path
from one_app import views
app_name='one_app'#use for template tagging, check href in users.html for usage.

urlpatterns = [
    path('', views.index, name="home"),
    path('users', views.users, name="users"),
    path('user/create', views.user_form, name='createUser'),
    path('user/create2', views.user_model_form, name='createUser2'),
    path('about', views.about, name="about"),

    path('index', views.home2, name="index"),
    path('register', views.register, name="register"),
    path('user-login', views.user_login, name="user_login"),
    path('user-logout', views.user_logout, name="user_logout"),
    path('dashboard', views.dashboard, name="dashboard")
]