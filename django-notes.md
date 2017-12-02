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


## Useful URL Patterns
####Primary Key AutoField
Regex   (?P<pk>\d+)
Example url(r'^questions/(?P<pk>\d+)/$', views.question, name='question')
Valid URL   /questions/934/
Captures    {'pk': '934'}

####Slug Field
Regex   (?P<slug>[-\w]+)
Example url(r'^posts/(?P<slug>[-\w]+)/$', views.post, name='post')
Valid URL   /posts/hello-world/
Captures    {'slug': 'hello-world'}

####Slug Field with Primary Key
Regex   (?P<slug>[-\w]+)-(?P<pk>\d+)
Example url(r'^blog/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', views.blog_post, name='blog_post')
Valid URL   /blog/hello-world-159/
Captures    {'slug': 'hello-world', 'pk': '159'}

####Django User Username
Regex   (?P<username>[\w.@+-]+)
Example url(r'^profile/(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile')
Valid URL   /profile/vitorfs/
Captures    {'username': 'vitorfs'}

####Year
Regex   (?P<year>[0-9]{4})
Example url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive, name='year')
Valid URL   /articles/2016/
Captures    {'year': '2016'}

####Year / Month
Regex   (?P<year>[0-9]{4})/(?P<month>[0-9]{2})
Example url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive, name='month')
Valid URL   /articles/2016/01/
Captures    {'year': '2016', 'month': '01'}