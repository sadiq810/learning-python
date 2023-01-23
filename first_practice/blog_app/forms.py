from django import forms
from blog_app import models


class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ("title", "detail", "image")
