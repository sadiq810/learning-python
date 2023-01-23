## Create migrations in your app like app_one and in the models.py file.

## To run migration
 - python manage.py migrate

## Register migration to your app (connect models to app).
- python manage.py makemigrations one_app

## To interact your python shell
- python manage.py shell

## To import first model in shell
- from one_app.models import Topic
- t = Topic(top_name='first topic')
- t.save()

#to exit the shell
- quit()

## To use your models with admin panel, first register your models in one_app/admin.py
## To interact with admin, we need to create superuser using below command.
- python manage.py createsuperuser


## to install faker
- pip install Faker

## To add support for images then install image library or in case of any issue like jpeg disabled etc then follow second command.

- pip install pillow
- pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"

#To install Argon two hasher
- pip install django[argon2]