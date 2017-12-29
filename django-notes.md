# Basic Commands
#### Create project
```django-admin startproject projectname```

#### Add app to project
```django-admin startapp appname```

#### Run server
```python manage.py runserver```

#### Run python shell with projects and Django loaded
```python manage.py shell```

## Superusers
#### Create superuser
```python manage.py createsuperuser```

##### myprojects admin credentials
user: admin
password: thatsmybird1

## Migrations and Database
#### Generate SQL migrations to create database from models
```python manage.py makemigrations```

#### Inspect SQL instructions for migration
```python manage.py sqlmigrate appname 0001```

#### Apply migrations
```python manage.py migrate```

## Testing
#### Run test classes defined in tests.py
```python manage.py test```

#### Test with higher verbosity
```python manage.py test --verbosity=2```

## Interactive Shell Cheatsheet
###### Create an instance of your model
```
from appname.models import MyModel
# either using your base class
modelInstance = MyModel(param1=val, param2=...)
# or using the Model Manager
modelInstance = MyModel.objects.create(param1=val, param2=...)
```
###### Persist a model instance in the database
```modelInstance.save()```

###### List all existing instances of model
```MyModel.objects.all()```

###### Return instance by parameter 
```
# other fields can be used, but must only return one object
thisInstance = MyModel.objects.get(id=1)
```
###### Check settings
```
from django.conf import settings
# for example
print(settings.BASE_DIR)
```

###### Exit the interactive shell
```exit()```

# Concepts
### Projects
A _project_ is a collection of configurations and apps. One project can be composed of multiple apps, or a single app.

A _project_ has the following folder structure:

* manage.py: a shortcut to use the django-admin command-line utility. It’s used to run management commands related to our project. We will use it to run the development server, run tests, create migrations and much more.
* \__init__.py: this empty file tells Python that this folder is a Python package.
* settings.py: this file contains all the project’s configuration. We will refer to this file all the time!
* urls.py: this file is responsible for mapping the routes and paths in our project. For example, if you want to show something in the URL /about/, you have to map it here first.
* wsgi.py: this file is a simple gateway interface used for deployment. 

#### Creating a project
1. Run ```django-admin startproject projectname```.

### Apps
An _app_ is a Web application that does something. An app usually is composed of a set of models (database tables), views, templates, tests.

An _app_ has the following folder structure:

* migrations/: here Django store some files to keep track of the changes you create in the models.py file, so to keep the database and the models.py synchronized.
* admin.py: this is a configuration file for a built-in Django app called Django Admin.
* apps.py: this is a configuration file of the app itself.
* models.py: here is where we define the entities of our Web application. The models are translated automatically by Django into database tables.
* tests.py: this file is used to write unit tests for the app.
* views.py: this is the file where we handle the request/response cycle of our Web application.

#### Creating an app
1. Run ```django-admin startapp appname```.
2. Go to settings.py and add its name to the INSTALLED_APPS list.

### Views
Views are python functions that receive a HttpRequest object and return a HttpResponse object. 

* defined in views.py
* urls.py defines for what requests the application will serve which views.

### Models
The models define the properties and behaviors of the entities that make up an application. For instance, in a typical message board application, the __Boards__, __Topics__, __Posts__, and __Users__ would all be models.

* Models are defined in appname/models.py
* Every model is a class
* Fields like __CharField__, __DateTimeField__, and __ForeignKey__ are all methods of the __models__ object, which can be imported using ```from django.db import models```. Each field defined using these methods will be automatically stored in a database.

### Urls
Use regular expressions and the ```url()``` function to define your _urls_ and enable http access to your website pages. It has the following definition:
```
def url(regex, view, kwargs=None, name=None):
# 
```
* regex: A regular expression for matching URL patterns in strings. Note that these regular expressions do not search GET or POST parameters. In a request to http://127.0.0.1:8000/boards/?page=2 only /boards/ will be processed.
* view: A view function used to process the user request for a matched URL. It also accepts the return of the django.conf.urls.include function, which is used to reference an external urls.py file. You can, for example, use it to define a set of app specific URLs, and include it in the root URLconf using a prefix. We will explore more on this concept later on.
* kwargs: Arbitrary keyword arguments that’s passed to the target view. It is normally used to do some simple customization on reusable views. We don’t use it very often.
* name: A unique identifier for a given URL. This is a very important feature. Always remember to name your URLs. With this, you can change a specific URL in the whole project by just changing the regex. So it’s important to never hard code URLs in the views or templates, and always refer to the URLs by its name.

### Routing
Routing is taken care of by the logic in _views.py_.
 There are two ways to resolve to a 404.
 
 * Use the _Http404_ object
```
from django.shortcuts import render
from django.http import Http404
from .models import Board

def home(request):
    # code suppressed for brevity

def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})
```
 * Use the get_object_or_404 function
```
from django.shortcuts import render, get_object_or_404
from .models import Board

def home(request):
    # code suppressed for brevity

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})
```

### Database
As aforementioned, fields using ```from django.db import models``` will automatically be stored in a SQL database. To use a database, do the following:
1. Define your fields using the methods of the __models__ class inside of your own classes in models.py
2. Run ```python manage.py makemigrations```. This will create a file of SQL statements called __0001_initial.py__ inside __boards/migrations__.
3. Inspect that the generated commands are correct by running ```python manage.py sqlmigrate appname 0001```.
4. Launch the database with ```python manage.py migrate```

### Using the interactive shell
The interactive shell is like the python shell with two differences:

* The project is added to the __sys.path__
* Django is already loaded
Launch the interactive shell using ```python manage.py shell```. When you are done, use ```exit()```.

### Django Template Engine
* Templates are kept in the _templates/_ folder
* Tell Django where to find the templates by editing the _settings.py_ file. Find the ```TEMPLATES``` variable and set its property ```DIRS``` like so: 
```
'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ]
```
#### Template Special Tags
###### Print variable
```{{ var }}```
###### Iterate through list
```
{% for var in mylist %}
...
{% endfor %}
```
###### Include url
```
{% url 'url_name' vars.var1 vars.var2 ... %}
```
###### Blocks (Reusing Templates)
Define in ```master.html``` (name in closing tag is not necessary):
```
{% block name %}Default Name{% endblock name %}
```
Define in inheriting page:
```
{% extends 'master.html' %}
...
{% block name %}Inheritor Name{% endblock name %}
```
You can also use ```{{ block.super }}``` to reuse the contents of the master page block.
###### Add CSRF to Form
```{% csrf_token %}```

### Test Cases
* Test classes are organized by the app
* Tests are found in _tests.py_ by default
* Make multiple test files by creating a folder called _tests/_ and copying your existing tests inside the folder
* Run all tests by using ```python manage.py test```

### Static Files
To include static files in your application:
1. Make a folder called _static_ in the root directory of your project.
2. Place all your static files in there.
3. In _settings.py_, under where it says ```STATIC_URL```, add this: ```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]```
4. (Optional) If you are hosting static files externally, then change the ```STATIC_URL``` to the domain of your host, such as ```https://static.mysite.com/```.
5. In the beginning of your html templates, include ```{% load static %}```.
5. Wherever you need a link to a static file in your html, include an appropriate link like ```{% static 'css/bootstrap.min.css' %}```.

### Forms API
In ```django.forms``` we have two basic kinds of form classes:

* __Form__ is used to handle general-purpose input
* __ModelForm__ is a subclass of __Form__ and is used to process data associated with a model

It is common to make a new file _app_name/forms.py_ to define the forms in your application.

### Admins
Create an admin:
1. ```python manage.py createsuperuser```
2. Allow a model to be managed with admin privileges: 
```
from django.contrib import admin
from .models import MyModel

admin.site.register(MyModel)
```
Then you can navigate to ```127.0.0.1:8000/admin/``` to manage your model


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
