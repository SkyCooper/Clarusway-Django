https://lms.clarusway.com/mod/lesson/view.php?id=3878&pageid=6798
#! What is Django?

# Django is a web framework based on Python that allows you to build web applications easily without all the installation or dependency issues that you usually encounter with other frameworks. It is free and open source, has a thriving and active community, great documentation, and many options for free and paid-for support.

#  It is used by many sites, including   Disqus, Instagram, Knight Foundation, MacArthur Foundation, Mozilla, National Geographic, Open Knowledge Foundation, Pinterest, and Open Stackas .

#? Features of Django
#* Versatility of Django 
# Django is able to create almost any kind of website. It can also work with any framework on the client side and can deliver content in any format such as HTML, JSON, XML, etc.

# *Security 
# Django takes security seriously and helps developers avoid many common security mistakes, such as SQL injection, cross-site scripting, cross-site request forgery and clickjacking. Its user authentication system provides a secure way to manage user accounts and passwords.

#* Scalability 
# Django uses a "shared-nothing" component-based architecture (each part of the architecture is independent of the others). Having a clear distinction between the various parts means that by adding hardware at any stage, it can scale for increased traffic: caching servers, database servers, or application servers. Instagram and Disqus are two Django based products that have millions of active users, this is taken as an example of the scalability of Django.

#* Portability 
# All the codes are written in Python for the Django framework, which runs on several platforms. This also results in Django running on several platforms, such as Linux , Windows, and Mac OS..

#! Why Django?
    # Fully functional framework that requires nothing else.
    # Easy to switch database in Django
    # It has built in admin interface
    # Easily create apps and integrate several of those and manage them under one admin panel.
    # Thousands of additional packages available.
    # It is very scalable.

#? How Django Works
# A web application waits for HTTP requests from the web browser (or other clients) on a conventional data based website. The application figures out what is needed based on the URL and likely information in the POST data or GET data when a request is made. It can then read or write information from a database or perform other tasks needed to fulfill the request, depending on what is needed. The application then returns a response to the web browser, often generating a dynamic HTML page for the browser to view by inserting the collected data into the HTML template placeholders.

# Django web applications typically group the code that handles each of these steps into separate files.

#* What is MVT (Model, View, and Template)
# A web-framework has a basic model view controller architecture software design pattern for developing web applications, but Django is a bit different in a good way. It implements concept of Model-View-Template (MVT). MVT is slightly different from MVC. In fact, the main difference between the two patterns is that Django itself takes care of the Controller part (Software Code that controls the interactions between the Model and View), leaving us with the template. The template is an HTML file mixed with Django Template Language (DTL).

# A user requests for a resource to the Django, Django works as a controller and check to the available resource in URL (urls.py file). If URL maps, a view (function) is called that interact with model and template, it renders a template. Django responds back to the user and sends a template as a response.

#* URLs: 
# Although it is possible to process requests through a single function from every single URL, writing a separate view function to handle each resource is far more manageable. To redirect HTTP requests to the appropriate view based on the request URL, a URL mapper is used. The URL mapper may also match a unique string or digit patterns that appear in a URL and transfer these as data to a view feature..
#* View: 
# A view is a request handler function that accepts requests from HTTP and returns HTTP responses. Views access the data needed to fulfill requests through models and delegate the response formatting to the templates.
#* Models: 
# A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
#* Template: 
# Django needs a convenient way to generate HTML dynamically. The most common approach relies on templates. A template contains the static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted.

#! Installation of Django
# Installing system-wide or in a Python virtual environment?
# When you install Python3 you get a single global environment that is shared by all Python3 code. While you can install whatever Python packages you like in the environment, you can only install one particular version of each package at a time.

#! ⚠️Note:
# Python applications installed into the global environment can potentially conflict with each other (i.e. if they depend on different versions of the same package).
# If you install Django in the default / global environment, then only one version of Django can be targeted on your device. If you want to build new websites (using Django's latest version) while also retaining websites that rely on older versions, this can be an issue.

# So we'll show you how to install django into a virtual environment step by step.

# To run the latest version of Django Framework on your system you would need Python 3 installed on your system. You just have to download the package from the official website, according to your operating system.
#! Note: 
# Installation of Django in Linux and Mac is similar, here showing it in windows, for Linux and mac just open terminal in place of command prompt and go through the following commands. (Try python3 and pip3 instead of python and pip)

# Check the versions of python and pip
python --version
pip --version
# Install virtual environment
pip install virtualenv

# Set virtual environment: navigate to the folder where you want to create your project and then enter the following:
virtualenv nameofyourvitualenv
# Change directory to your vitualenv
# (For Windows Users) Go to Scripts directory inside your virtualenv and activate virtualenv
cd Scripts
activate
# (For Linux and mac) Activate virtualenv:
source nameofyourvirtualenv/bin/activate
# Install Django
pip install django
# Return to your virtualenv directory
cd ..
# Start a project by following command
django-admin startproject nameofyourproject
# Change directory to your project
cd nameofyourproject
# Start the server by following command
python manage.py runserver
# To check wether server is running or not go to web browser and enter http://127.0.0.1:8000/ as url.
  
#? Project Structure
# We created our first Project. When you look at the project folder it contains basic files by default such as manage.py, settings.py etc. A simple project structure is enough to create a single page application. Here are the major files and there explanations. Inside the project folder there will be following files;

#* Project Structure
# Clarusway/__ init __.py: An empty file that tells Python that this directory should be considered a Python package.
# Clarusway/settings.py: As the name indicates it contains all the website settings. In this file we register any applications we create, the location of our static files, database configuration details, etc.
# Clarusway/urls.py: In this file we store all links of the project and functions to call. It is more common to delegate some of the mappings to particular applications, as you'll see later.
# Clarusway/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. It is used to help your Django application communicate with the web server.
# Clarusway/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. ASGI is the asynchronous successor to WSGI and provides a standard for both asynchronous and synchronous Python apps (whereas WSGI provided a standard for synchronous apps only).
# manage.py: A command-line utility that lets you interact with this Django project in various ways.For getting the full list of command that can be executed by manage.py type python manage.py help in the command window.

#? Create an App
# Each application you write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.

#! Projects vs. apps
# What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.


# To create your app, make sure you’re in the same directory as manage.py and type this command:
python manage.py startapp fscohort

#* App Directory Structure
# fscohort/__ init __.py: An empty file that tells Python that this directory should be considered a Python package.
# fscohort/admin.py: contains settings for the Django admin pages.
# fscohort/apps.py: contains settings for the application configuration.
# fscohort/models.py: contains a series of classes that Django’s ORM converts to database tables.
# fscohort/tests.py: contains test classes.

# To consider the app in your project you need to specify your project name in INSTALLED_APPS list as follows in settings.py:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # myapps
    'fscohort'
]

# Write your first view
# Let’s write our first view. Open the file fscohort/views.py and put the following Python code in it:

#* fscohort/views.py
#* HttpResponse is used to 
#* pass the information  
#* back to view 
from django.http import HttpResponse

#* Defining a function which 
#* will receive request and 
#* perform task depending  
#* upon function definition 
def index(request):

    #* This will return Hello, world. This is fscohort index page.
    #* string as HttpResponse 
    return HttpResponse("Hello, world. This is fscohort index page.")

# To call the view, we need to map it to a URL - and for this we need a URLconf.
# To create a URLconf in the fscohort directory, create a file called urls.py.
# In the fscohort/urls.py file include the following code:

# fscohort/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# The next step is to point the root URLconf at the fscohort.urls module. In Clarusway/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list, so you have:
# Clarusway/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('fscohort/', include('fscohort.urls')),
    path('admin/', admin.site.urls),
]

# The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

#* When to use include()
# You should always use include() when you include other URL patterns. admin.site.urls is the only exception to this.

# Now we have wired an index view into the URLconf. Verify it’s working with the following command:
python manage.py runserver

# Go to http://localhost:8000/fscohort/ in your browser, and you should see the text “Hello, world. This is fscohort index page.”, which you defined in the index view.

#? Login to Admin Site
# One of the most powerful parts of Django is the automatic admin interface that you can use to create, view, update, and delete records. It reads metadata from your models to provide a quick, model-centric interface where trusted users can manage content on your site.

# In order to login, we need to create a user who can login to the admin site. Run the following command:
python manage.py createsuperuser

# But, it'll give you an error.
# As you see in the error text we need to run python manage.py migrate command to apply some table to database. After run this command create your user again with python manage.py createsuperuser
 python manage.py migrate

# Enter your desired username and press enter:
# Enter your email adress:
# The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

# Now go to http://127.0.0.1:8000/admin/. You should see the admin's login screen.
# After you login, you should see a few types of editable content: groups and users. They are provided by django.contrib.auth, the authentication framework shipped by Django.