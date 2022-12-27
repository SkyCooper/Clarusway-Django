https://lms.clarusway.com/mod/lesson/view.php?id=10270&pageid=8672&startlastseen=no

#! Views
# The place where we will create the logic part of the backend structure is the views section, as in Django. While doing this, in views.py, we will use the serializers classes we created before.
# Like Django, DRF also has two types of views; function-based views (FBVs), and class-based views (CBVs).
# In the coming sections, we will see mixins and concrete views as well and it will make our work much easier.
# According to the views, we will also create our endpoints in the urls.py file that users will use to pull data from our databases. We can see the operations of the endpoints we will create using the postman platform. However, DRF offers us the Browsable API structure, which is very useful in this regard. DRF Browsable API supports generating human-friendly HTML output for each resource(endpoints) when the HTML format is requested. These pages allow for easy browsing of resources, as well as forms for submitting data to the resources using POST, PUT, and DELETE.

#! Function Based Views
# Now, we'll use function-based views. Open your fscohort_api/views.py and write this code.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from fscohort.models import Student


@api_view(['GET', 'POST'])
def student_list(request):
    """
    List all students, or create a new student.
    """
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    """
    Retrieve, update or delete student.
    """
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# line 11 to use status code in our views, we import status module. You can see the full list of status code here

# line 12 we imported Response class which allows you to return content that can be rendered into multiple content types, depending on the client request.

# line 13 we import api_view decorator. We must use this when writing function-based views to use DFR.

# line 25 we serialized the student object and used many=True. When you serialize more than one object you have to use many=True.

# line 29 we used request.data. request.data returns the parsed content of the request body. This is similar to the standard request.POST. It supports parsing the content of HTTP methods other than POST, meaning that you can access the content of PUT and PATCH requests.

# As you can see it is very similar to Django function-based views. Now we need to configure our URLs.

# Open your clarusway/urls.py and add this URL.
urlpatterns = [
    ........
    path('api/', include('fscohort_api.urls'))
]

# Open your fscohort_api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list),
    path('< int:pk >/', views.student_detail),
]

# When you go to http://127.0.0.1:8000/api/ you can see a browsable api from the django rest framework.
# You can list all students and add a new student here and test your endpoint.