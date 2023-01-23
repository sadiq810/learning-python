import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_practice.settings')

import django
django.setup()

from faker import Faker
from django.contrib.auth.models import User

fakergen = Faker()

from blog_app.models import Blog

def user():
    user = User.objects.get_or_create(first_name="test", last_name="user", username="testuser", password="testtest", email="test@test.com")[0]
    return user

def populate(N=5):
    usr = user()

    for i in range(N):
        title = fakergen.sentence(nb_words=3)
        slug = fakergen.slug()
        detail = fakergen.sentence(nb_words=100)

        Blog.objects.create(title=title, slug=slug, detail=detail, user=usr)


if __name__ == "__main__":
    print("Populating blogs table")
    populate(20)
    print("Blogs populated.")