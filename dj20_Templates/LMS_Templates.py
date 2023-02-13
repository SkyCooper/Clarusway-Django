# LMS --> https://lms.clarusway.com/mod/lesson/view.php?id=7004&pageid=6866

#! Why Django Templating?
# In the last section, we created a view that returns single line of HtttpResponse.

def student_num(request):
    num_of_stdnt = Student.objects.count()
    return HttpResponse("FS Cohort has {} students". format(num_of_stdnt))

# But what if our project is too big and we need fully designed web page for every view. Imagine putting all that code in a single view. It'll be very complex.

# Django is a web framework and that makes it very important to dynamically serve HTML pages, so Django has a special component, Django Templates, to do that.

#! What are Django Templates
# Basically, a template in Django is written in a HTML , CSS and Javascript in an .html file. The Django framework effectively handles and generates dynamically visible HTML web pages for end-users.

# The main goal of the Django templates is to distinguish the representation of the data from the data itself. That means that the browser portion is only intended to render the HTML sent to it by the server, and Django itself gives all the relevant data to the template. This makes the process much smoother and easier to render pages, since both the front-end and back-end have less clutter.

#! Django Template Language(DTL)
# A Django template is a text document or a Python string marked-up using the Django template language. Some constructs are recognized and interpreted by the template engine. The main ones are variables and tags.

# A template is rendered with a context. Rendering replaces variables with their values, which are looked up in the context, and executes tags.

# The syntax of the Django template language involves three constructs.

#* Variables:
# Outputs a value from the context, which is a dict-like object mapping keys to values. Variables are surrounded by {{ and }} like this. For example:

Simple Variables: {{ title }}
Object Attributes: {{ page.title }}
Dictionary Lookups: {{ dict.key }}
List Indexes: {{ list_items.0 }}

#* Tags:
# Provide arbitrary logic in the rendering process. Tags are surrounded by {% and %} like this. There are many built-in tags. Some example functions performed by template tags are:

Display Logic: {% if %}...{% endif %}
Loop Control: {% for x in y %}...{% endfor %}
Block Declaration: {% block content %}...{% endblock %}
Content Import: {% include "header.html" %}
Inheritance: {% extends "base.html" %}

#* Filters:
# Transform the values of variables and tag arguments. You apply a filter to a variable using the | (pipe) character. There are many built-in filters, here are some examples:

Change Case: {{ name|title }}
Truncation: {{ post_content|truncatewords:50 }}
Date Formatting: {{ order_date|date:"D M Y" }}
List Slicing: {{ list_items|slice:":3" }}

# Template Folder
# In your Clarusway/settings.py file default template settings look like this:

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# In line 58 'APP_DIRS' is True. This means Django will look for templates folder in each app listed in INSTALLED_APPS.

# Let's create templates folder for our fscohort app. But we need to namespacing our templates. We add a folder named after the app to our templates folder. Your directory tree should look like this.


# If you don't want to put your templates folder in INSTALLED_APPS, you have to tell Django where to find your templates by adding a path to the DIRS settings.(Line 81)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'clarusway/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


#! Displaying a Template
# We created our template folder in fscohort app. Now, we can create our template. Let's create home.html and student_list.html files in fscohort/templates/fscohort folder.

#? fscohort/templates/fscohort/home.html

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Home</title>
# </head>
# <body>
#     <h1>FSCOHORT Home Page.</h1>
#     <p>Hello, world. This is fscohort Home page from app folder.</p>
# </body>
# </html>

#? fscohort/templates/fscohort/student_list.html

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Student List</title>
# </head>
# <body>
#     <ul>
#         {% for student in students %}
#         <!-- Display attributes of instance -->
#         <li>{{ student.first_name }} {{ student.last_name }}</li>
#         {% endfor %}

#     </ul>
#     <p>Total Students: {{ num }}</p>
# </body>
# </html>

# To display our templates, we must modify our views.

#? fscohort/views.py

from django.shortcuts import render
# from django.http import HttpResponse
from .models import Student

def index(request):
    # return HttpResponse("Hello, world. This is fscohort index page.")
    return render(request, 'fscohort/home.html')

def student_num(request):
    students = Student.objects.all()
    num_of_stdnt = Student.objects.count()
    context = {
        'students': students,
        'num': num_of_stdnt
    }
    return render(request, 'fscohort/student_list.html', context)

# For our new views, we have replaced the HttpResponse() with render().
# render() is a special Django helper function that creates a shortcut for communicating with a web browser.

# In the previous code, we simply returned some text. However, when we want to use a template, Django must load the template, create a context which is a dictionary of variables and associated data passed back to the browser and return an HttpResponse.

# In Django, we can code each of these steps separately but it is more common and easier to use Django render() function. It provides a shortcut that execute all steps in a single function.

# Now, when you navigate http://127.0.0.1:8000/fscohort and 
# http://127.0.0.1:8000/fscohort/num you should see your new templates.

#? /fscohort
FSCOHORT Home Page.
Hello, world. This is fscohort Home page from app folder.


#? /fscohort/num
- Henry Forester
- Edward Benedict
- Mccarthy Silva
- Mark Madison
- Adam Flyer
- Joe BLUE
Total Students: 6