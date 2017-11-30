## Basics
#### Create project
django-admin startproject projectname

#### Add app to project
django-admin startapp appname

#### Run server
python manage.py runserver

#### Run python shell with projects and Django loaded
python manage.py shell

## Superusers
#### Create superuser
python manage.py createsuperuser

user: admin
password: thatsmybird1

## Migrations and Database
#### Generate SQL migrations to create database from models
python manage.py makemigrations

#### Inspect SQL instructions for migration
python manage.py sqlmigrate appname 0001

#### Apply migrations
python manage.py migrate

## Testing
#### Run test classes defined in tests.py
python manage.py test

#### Test with higher verbosity
python manage.py test --verbosity=2