https://lms.clarusway.com/mod/lesson/view.php?id=6932

#! What is views in Django?
# Whenever you visit a page on the internet, your browser sends a request which contains things like headers (metadata about who you are), parameters (variables), HTTP process, and sometimes a body of data. Upon doing so, you expect to receive a response in return, which consists of much the same pieces. You should expect a different answer to come back to you, depending on the type of the request you make.

# Given that a view's only purpose is to handle user requests, your views should be designed to do nothing more than parse requests to serve a proper response.

#? Django Views
# Django view is a Python class and/or a function that takes a Web request and returns a Web response. It's a place where we put the "logic" of our application. It will request information from the model you created before and pass it to a template.

# We wrote our first view in the Introduction section. Now add this view in your fscohort/views.py
def student_num(request):
    num_of_stdnt = Student.objects.count()
    return HttpResponse("FS Cohort has {} students". format(num_of_stdnt))

# We need to display this view at a particular URL. Open your fscohort/urls.py file and add this url conf.
urlpatterns = [
    path('', views.index, name='index'),
    path('num/', views.student_num, name='student_num'),
]

# We configured our main project Claruswa/urls.py file in the Introduction section.
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('fscohort/', include('fscohort.urls')),
    path('admin/', admin.site.urls),
]

# Django will redirect everything comes into http://127.0.0.1:8000/fscohort to fscohort.urls and look for further instruction there. So when you visit the http://127.0.0.1:8000/fscohort/num, this pattern tells the django views.student_num is the right place to go.

# And student_num views will return a HttpResponse object that contains the generated response.
Fs Cohort has 5 students.

#? Type of Views
# Django has two types of views; function-based views (FBVs), and class-based views (CBVs).

#* Function-Based Views:
# Function based views are writter using a function in python which recieves as an argument HttpRequest object and returns an HttpResponse Object.

# This function is easy in implementing and it’s quite useful but the main drawback is that on a large size Django project, there are generally many similar functions in the views. One instance is that all objects of a Django project have CRUD operations, therefore this code repeats unnecessarily. This was the main reason for the creation of Generic Class-based views.

#* Class-Based Views:
# Class-based views provide an alternative way to implement views as Python objects instead of functions. They do not replace function-based views, but have certain differences and advantages when compared to function-based views:
    # Organization of code related to specific HTTP methods (GET, POST, etc.) can be addressed by separate methods instead of conditional branching.
    # Object oriented techniques such as mixins (multiple inheritance) can be used to factor code into reusable components.