https://lms.clarusway.com/mod/lesson/view.php?id=10270&pageid=8672&startlastseen=no

#! Class Based Views
# Using the Class-Based structure we do the same operations that we did use the Function Base structure on the previous page. As you can see below, it provides a more organized code structure. The logic and codes are almost the same. Review the codes, please.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentSerializer
from fscohort.models import Student


class StudentList(APIView):
    
    def get(self, request):
        students = Student.objects.all()
        serializer =StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentGetUpdateDelete(APIView):
    
    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        #student = get_object_or_404(Student, id=id)
        student = self.get_object(id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def post(self, request, id):
        student = self.get_object(id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message":"Student updated"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def  delete(self, request, id):
        student = self.get_object(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# - line 8 We imported APIVıew class and inherited our classes from APIVıew class.

# Then configure our urls.py file:
from django.urls import path
from . import views as api_views

urlpatterns = [
    path("", api_views.StudentList.as_view(), name="list"),
    path("/", api_views.StudentGetUpdateDelete.as_view(), name="detail"),
]

# When you go to http://127.0.0.1:8000/api/ you can see a browsable API from the DRF and the same result as Functional Base views

#! Generic Views And Mixins
# Since the operations we perform for CRUD operations in Django are generally similar operations, so structures that perform these operations for us in the background have been developed. In this way, we get rid of rewriting the same codes and we do the same work with less code.
# For this purpose, GenericAPIViews and Mixins have been created by DRF. Generic APIViews are inherited from APIView that we use in Class-Based Views and give them extra features. GenericApiViews are often used with mixins. Mixins adds .create() and .list() capabilities to GenericAPIViews. You can think of them like .get() and .post()
# Let's write the same operations with GenericAPIViews and Mixins:

from fscohort.models import Student
from .serializers import StudentSerializer
from rest_framework import generics, mixins

class StudentDetail(generics.GenericAPIView,mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin ):
    
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = "id"
    
    def get(self, request, id):
        return self.retrieve(request)
             
    def put(self, request, id):
        return self.update(request, id)
    
    def delete(self, request, id):
        return self.destroy(request,id)


class Student(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
 
        
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
# line 78 we imported generics and mixins from rest_framework
# line 82 we define the serializer_class (the name is standard) which we created before.
# line 83 We define the query_set (the name is standard) according to the view logic we will set up
# line 84 Lookup_field: It specifies which field we will call the objects from. It should be unique

# NOTE: We use lookup_field and id as we will call a specific object for GET, PUT, DELETE operations from django.urls import path from .views import Student, StudentDetail Let's configure urls.py file :
# When you go to http://127.0.0.1:8000/api/list you can see a browsable API from the DRF, Student list and a form for create student

# If you want to view a specific student object you should use the id of the student. For example, http://127.0.0.1:8000/api/16 endpoint brings us the student whose id number is 16.
# we can see GET, PUT, DELETE options for this student in the browsable API.


#! Concrete Views
# We learned what was going on in the background with GenericAPIView and Mixins. Our main goal is to learn Concrete views. Concrete views offer us all the functionality we will need with much less code.

# Each concrete view consists of a GenericAPIView and associated Mixins. for example: ListCreateApiView is a combination of ListModelMixin, CreateModelMixin and GenericAPIView. 


# So ConcreteViews are the easiest views to write and read. Let's code the same operations with concrete views
from rest_framework import generics

class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    

class StudentGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = "id"

# Let's configure urls.py file :
urlpatterns = [
    path("list/", StudentList.as_view(), name="list"),
    path("list/", StudentGetUpdateDelete.as_view(), name="detail"),

]

# Let's view same response in the Browsable API ( http://127.0.0.1:8000/api/list) 
# For a specific student ( http://127.0.0.1:8000/api/list/16)
