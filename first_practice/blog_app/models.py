from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=False, null=True)
    detail = models.TextField(blank=True)
    image = models.ImageField(upload_to="blog_images", blank=True)

    def __str__(self):
        return self.title