# Badger Buddy

# Setup
Install Django: [Link](https://docs.djangoproject.com/en/3.1/intro/install/)\
This project was developed with Django 3.1. 

**<code> pip install django-registration </code> for registration pages to work**


# Admin user
### Username: admin
### Password: password

# Useful Commands and Common Workflows:
### All commands assume you are in the directory containing manage.py

## Run development server
python manage.py runserver

## Create and display a view
1. Create view function in \<app-name\>/views.py
2. Add path to view in urlpatterns list in \<app-name\>/urls.py \
   (May need to add path to urlpatterns list in badger_buddy/urls.py as well, e.g. if app is new)

## Add / edit models
1. Add / edit model classes in \<app-name\>/models.py
2. Store changes to models as migrations: python manage.py makemigrations
3. Apply migrations to database: python manage.py migrate

## Create new app and install app to project
1. Create app: python manage.py startapp \<app-name\>\
   (Notice app has a configuration class in \<app-name\>/apps.py)
2. Install app to a project: in INSTALLED_APPS list (badger_buddy/settings.py), add a reference to the app's configuration class

## Django database querying
Overview with examples: [Link](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#playing-with-the-api)\
Get everything in a table: \<model-name\>.objects.all()\
Lookup: \<model-name\>.objects.filter(), \<model-name\>.objects.get()\
RelatedManager useful for querying one-to-many or many-to-many relations: [Link](https://docs.djangoproject.com/en/3.1/ref/models/relations/)\
Double underscores to follow relationships (see example at end of overview linked above)

## Give admin access to model objects
1. In \<app-name\>/admin.py, import \<model-name\> from .models
2. In \<app-name\>/admin.py, register the model: admin.site.register(\<model-name\>)

## Add Bootstrap reference for any html template
Insert <code> {% include "style/bootstrap.html" %}  </code>  at the top <br>
Usage guide: https://getbootstrap.com/docs/4.3/components/

## Common templates such as headers and footers
Use block-content and endblock. 
More details: https://docs.djangoproject.com/en/3.1/ref/templates/language/#id1

## Linking js or css files
Consider these as static files: https://docs.djangoproject.com/en/3.1/howto/static-files/ <br>
Linking jsx or react files: transfer to js file first: https://reactjs.org/blog/2013/08/19/use-react-and-jsx-in-python-applications.html
