from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#? CLASS BASED VIEW
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

#? my imports,
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer

#? pagination, filter, search
from .pagination import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

@api_view(['GET']) #? yazılmasa bile default GET olarak çalışır.
def home(request):
    return Response({'home':'This is HOME page ✌'})

#? ==========================================================
#? VIEWSETS
#? ==========================================================

#! Tek bir view oluşturarak hem pk/id (lookup) gerekli olmayan,(GET, POST)
#! Hem de pk/id (lookup) isteyen bütün bütün işlemleri yapabiliyoruz. (GET, PUT, PATCH, DELETE)

class StudentMVS(ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    #? pagination
    pagination_class = CustomPageNumberPagination
    # pagination_class = CustomLimitOffsetPagination
    # pagination_class = CustomCursorPagination
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] #? hepsi beraber yazılabilir,
    
    #? filter
    # pip install django-filter
    # yazılan kelimenin aynısını arar,
    # mesela name için data içinde cooper varsa coop yazınca bulmaz.
    
    # filter_backends = [DjangoFilterBackend]                 #? hangi filitrelemeyi kullanacak,
    filterset_fields = ["id", "first_name", "last_name"]      #? nerede filitrelemeyi kullanacak,
    
    #? search
    # ilave bir paket yüklemeye gerek yok,
    # yazılan kelimenin içinde arama yapar,
    # mesela name için data içinde cooper varsa coop yazınca bulur.
    # aynı zamanda last_name de aramaya dahilse macoopland gibi yazan birşeyide bulur ve 2 sonuç getirir.
    
    # filter_backends = [SearchFilter]                        #? hangi aramayı kullanacak,
    search_fields = ["first_name", "last_name"]               #? nerelerde arama yapacak,
    # search_fields=['^first_name']                           #? baş harfine göre arama yapmak için,
    
    #? ordering
    # filter_backends = [OrderingFilter]                   #? hangi sıralamayı kullanacak,
    ordering_fields = ['first_name','last_name']  #* filter boxta hangi seçenekler çıksın istiyorsanız onu yazıyorsunuz
    ordering = ['last_name']  #* default olarak ilk açıldığında buraya yazdığımıza göre sıralıyor
    
    
    #? action decarator  ile viewset'lere extra kabiliyetler yazabiliyoruz..
    #? bir class yapısı içinde olduğumuzdan içine method yazabiliriz.
    
    @action(detail=False, methods=["GET"])
    
    #? tek (spesifik) bir öğrenci olmadığı için False,  default method GET
    #? action ile yeni bir endpoint oluşuyor, ....../api/student/student_count(fonksiyonun ismi)  olan.
    #!  ....../api/prefix/url_path(fonksiyonun ismi) (dokümanda böyle açıklanmış)
    
    def student_count(self, request):
        count = {"student-count" : self.queryset.count()}
        #? queryset içindeki objeleri sayar (yani Student class'ından üretilmiş bütün objeler, öğrenciler)
        return Response(count)

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

