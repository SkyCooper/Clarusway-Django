from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# CLASS BASED VIEW
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

#? my imports,
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer

#? pagination, filter, search
from .pagination import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

#? Permission
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


@api_view(['GET']) #? yazılmasa bile default GET olarak çalışır.
def home(request):
    return Response({'home':'This is HOME page ✌'})


class StudentMVS(ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    #? pagination
    pagination_class = CustomPageNumberPagination
    # pagination_class = CustomLimitOffsetPagination
    # pagination_class = CustomCursorPagination
    
    #? filter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["id", "first_name", "last_name"]
    
    #? search
    search_fields = ["first_name", "last_name"]
    # search_fields=['^first_name']  #baş harfine göre arama yapmak için,
    ordering_fields = ['first_name','last_name']  #* filter boxta hangi seçenekler çıksın istiyorsanız onu yazıyorsunuz
    ordering = ['last_name']  #* default olarak ilk açıldığında buraya yazdığımıza göre sıralıyor
    
    #? permission
    #* herkes CRUD yapabilir
    # permission_classes = [IsAuthenticated]
    
    #* sadece admin olan CRUD yapabilir
    permission_classes = [IsAdminUser]
    
    #* admin olan herşeyi yapar, olmayan sadece GET(read) yapar.
    # permission_classes = [IsAuthenticatedOrReadOnly]
    
    #? action decarator  ile viewset'lere extra kabiliyetler yazabiliyoruz.
    @action(detail=False, methods=["GET"])
    #? tek (spesifik) bir öğrenci olmadığı için False,  default method GET
    #? action ile yeni bir endpoint oluşuyor, ....../api/student/student_count(fonksiyonun ismi)  olan.
    #!  ....../api/prefix/url_path(fonksiyonun ismi) (dokümanda böyle açıklanmış)
    
    def student_count(self, request):
        count = {"student-count" : self.queryset.count()}
        #? queryset içindeki objeleri sayar (yani Student class'ından üretilmiş bütün objeler, öğrenciler)
        return Response(count)


#* Authentication => bir kişinin ya da bir şeyin iddia ettiği olduğunu doğrulamak için yapılan işlemdir. Bu genellikle bir kullanıcı adı ve parola gibi kimlik bilgileri ya da bir parmak izi veya yüz tanıma gibi biyometrik veriler kullanılarak yapılır.

#* Authorization =>  doğrulanmış kullanıcının izinlerine göre belirli kaynaklara veya eylemlere erişimi verme veya reddetme işlemidir. Örneğin, doğrulanmış bir kullanıcının belirli belgeleri okumaya izin verilmiş olabilir, ancak düzenleme veya silme yetkisi olmayabilir.


class PathMVS(ModelViewSet):
    
    queryset = Path.objects.all()
    serializer_class = PathSerializer
    
    @action(detail=True) 
    #? tek (spesifik) bir Path için işlem yapılacağından True, default method GET (belirtmeye gerek yok)
    #? action ile yeni bir endpoint oluşuyor, ....../api/path/1/student_names(fonksiyonun ismi)  olan.
    #!  ....../api/prefix/lookup/url_path(fonksiyonun ismi) (dokümanda böyle açıklanmış)
    
    def student_names(self, request, pk=None):
        path = self.get_object()
        students = path.students.all()
        #? Her path'de bulunan öğrenci isimlerini getiren bir method yazdık.
        return Response([i.first_name for i in students])

