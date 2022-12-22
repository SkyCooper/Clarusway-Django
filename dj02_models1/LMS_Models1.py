https://lms.clarusway.com/mod/lesson/view.php?id=6897
#! Models
# A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table. We can use the Django admin panel to create, retrieve, update or delete model fields and various similar operations.

# Each model is a Python class that subclasses django.db.models.Model.
# Each attribute of the model represents a database field.
# With all of this, Django gives you an automatically-generated database-access API
# Let's create our first model. Open the fscohort/models.py file and write this code.
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField() 

# first_name, last_name and number are fields of the model. Each field is specified as a class attribute, and each attribute maps to a database column.
# CharField and IntegerField are field types which tells the database what kind of data to store. There are many types of fields. You can view the full list here.
# max_length is field argument which is required for Charfield. There’s also a set of common arguments available to all field types. All are optional. You can view the full list of field option here.
# The above Student model would create a database table like this :
    CREATE TABLE Student (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name  varchar(30) NOT NULL,
        last_name  varchar(30) NOT NULL,
        number  INT NOT NULL,
    );

# An id field is added automatically to the model by Django.
# Run this command;
python manage.py makemigrations fscohort

# By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

# Now run this command;
python manage.py migrate 

# The migrate command takes all the migrations that haven’t been applied and run them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.

# Now, we need to tell the admin that the Student model has an admin interface. To do this, open the fscohort/admin.py file and edit it like this.
from django.contrib import admin
from .models import Student
admin.site.register(Student)

# If your server is not running start it python manage.py runserver

# We already create our super user. If you didn't create, create it python manage.py createsuperuser. Then login to your admin page. After you login, you should see your model on the admin page.

#! Database
# Django in its 'out-of-the-box' state is set up to communicate with SQLite -- a lightweight relational database included with the Python distribution. So by default, Django automatically creates an SQLite database for your project.

# In addition to SQLite, Django officially supports five databases:
    #* PostgreSQL
    #* MySQL
    #* Oracle
    #* MariaDB (Django 3 only)
# The Django configuration to connect to a database is done inside the settting.py file of a Django project in the DATABASES variable.
#* Database
#* https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#! Django ORM and Making Queries
#? Django ORM
# One of the most powerful features of Django is its Object-Relational Mapper (ORM), which provides an elegant and powerful way to interact with the database like you would with SQL. You don't need to write SQL queries for the database operations. ORM, as from the name, maps objects attributes to respective table fields. It can also retrieve data in that manner.

#? Making queries
# Once you’ve created your data models, Django automatically gives you a database-abstraction API (ORM) that lets you create, retrieve, update and delete objects. We'll see some most common Query methods. You can see the full list of methods here.

# Django Shell
# The Django shell is a Python shell that gives you access to the database API included with Django. The database API is a set of Python methods that allow you to access the project database from the data model.

# Open your console and type this command:
$ python manage.py shell

# Now, you're in the Django interactive console.

(InteractiveConsole)
>>> 
# From now on we'll execute our commands here.

#* Creating objects:
# First, we need to import our Student model
>>> from fscohort.models import Student

# Now, create our first object.
>>> s1 = Student(first_name="Henry", last_name="Forester", number=123)

# After that, we need to save it to the database.
>>> s1.save()

# Create more objects
>>> s2 = Student(first_name="Edward", last_name="Benedict", number=321) 
>>> s2.save()
>>> s3= Student(first_name="Mccarthy", last_name="Silva", number=456)
>>> s3.save()
>>> s4 = Student(first_name="Mark", last_name="Madison", number=654) 
>>> s4.save()

# To create and save an object in a single step, we can use the create() method.
>>> s5 = Student.objects.create(first_name="Adam", last_name="Flyer", number=789)

#* Retrieving all objects
# The simplest way to retrieve objects from a table is to get all of them. To do this, use the all() method
>>> all_students = Student.objects.all()
>>> print(all_students) 
<QuerySet [<Student: Student object (2)>, <Student: Student object (3)>, <Student: Student object (4)>, <Student: Student object (5)>, <Student: Student object (6)>]>

# When you print out all_students it returns a QuerySet (collection of objects from your database) of all the objects in the database. If you want to see your queryset more human readable format, you can modify your model like this;
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name) #* Now it returns firt_name + last_name instead of Student object

# Now, exit() your shell and reconnect and run the same code again. You should see this output.
<QuerySet [<Student: Henry Forester>, <Student: Edward Benedict>, <Student: Mccarthy Silva>, <Student: Mark Madison>, <Student: Adam Flyer>]>

#* Retrieving a single object
# If you know there is only one object that matches your query, you can use the get() method.
>>> g1 = Student.objects.get(first_name="Henry") 
>>> print(g1) 
Henry Forester

#* Retrieving specific objects with filters
# The QuerySet returned by all() describes all objects in the database table. Usually, though, you’ll need to select only a subset of the complete set of objects.

# filter(): Returns a new QuerySet containing objects that match the given lookup parameters.
>>> f1 = Student.objects.filter(first_name__startswith="m")      
>>> print(f1) 
<QuerySet [<Student: Mccarthy Silva>, <Student: Mark Madison>]>

#!   Note: There are two underscore characters (_) between first_name and startswith. Django's ORM uses this rule to separate field names ("first_name") and operations or filters ("startswith").

# exclude(): Returns a new QuerySet containing objects that do not match the given lookup parameters.

>>> e1 = Student.objects.exclude(first_name__startswith="m") 
>>> print(e1) 
<QuerySet [<Student: Henry Forester>, <Student: Edward Benedict>, <Student: Adam Flyer>]>

# Ordering and Limiting QuerySets
>>> Student.objects.order_by("first_name")[:2]  
<QuerySet [<Student: Adam Flyer>, <Student: Edward Benedict>]>

# ⚠️Note:  Negative indexing (Student.objects.all()[-1]) is not supported.