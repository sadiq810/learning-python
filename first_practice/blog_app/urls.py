from django.urls import path
from blog_app.views import dashboard, newBlog

app_name = "blog_app"

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('new-blog', newBlog, name="newBlog"),
]