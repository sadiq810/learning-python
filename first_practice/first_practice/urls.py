"""first_practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog_app.views import index, detail, user_register, user_login, user_logout

urlpatterns = [
    path('', index, name="index"),
    path('detail', detail, name="detail"),
    path('blog/', include('blog_app.urls')),
    path('user-login', user_login, name="user-login"),
    path('user-register', user_register, name="user-register"),
    path('user-logout', user_logout, name="user-logout"),
    path('admin/', admin.site.urls),
]
