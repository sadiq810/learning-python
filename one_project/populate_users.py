import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'one_project.settings')

import django
django.setup()

from faker import Faker

fakergen = Faker()

from one_app.models import Users

def populate(N=5):
    for i in range(N):
        fname = fakergen.first_name()
        lname = fakergen.last_name()
        uemail = fakergen.email()

        Users.objects.create(first_name= fname, last_name=lname, email=uemail)



if __name__ == '__main__':
    print("Populating users list.")
    populate(20)
    print('Users list populated.')