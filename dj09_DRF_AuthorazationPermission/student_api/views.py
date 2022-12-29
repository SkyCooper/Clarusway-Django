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

@api_view(['GET']) #? yazılmasa bile default GET olarak çalışır.
def home(request):
    return Response({'home':'This is HOME page ✌'})

# <===============  http methods  ===========================>
# - GET     --  (DB den veri çağırma,                   public)
# - POST    --  (DB de değişiklik yapma,(create)        private)
# - PUT     --  (DB de kayıt değişikliği(bütün data)    private)
# - DELETE  --  (DB de kayıt silme)
# - PATCH   --  (DB de kayıt değişikliği(kısmi update)  private)

    """  ilave açıklma :
# GET: Sunucudan bir belge veya veri almak için kullanılır. GET isteği yalnızca veriyi okumak için kullanılmalıdır, çünkü GET isteği tarayıcı ve proxy sunucuları tarafından önbelleğe alınabilir ve bu nedenle birkaç kez çalıştırılabilir.
# POST: Sunucuya bir belge veya veri göndermek için kullanılır. POST isteği, veritabanı güncelleştirmesi gibi veri oluşturan ve değiştiren işlemler için kullanılır.
# PUT: Sunucuya bir belge veya veri yüklemek için kullanılır. PUT isteği, bir belge veya verinin tamamının yerine koyulması için kullanılır.
# DELETE: Sunucudaki bir belge veya veriyi silmek için kullanılır.
# PATCH: Sunucudaki bir belge veya verinin bir parçasını değiştirmek için kullanılır.

# HEAD: Sunucudan bir belge veya verinin üstbilgilerini almak için kullanılır. HEAD isteği, GET isteğine benzerdir, ancak sunucudan geri dönen veri yoktur. Bu, sunucudaki bir belgenin varlığını veya önbelleklenme durumunu kontrol etmek için kullanılabilir.
# CONNECT: Sunucuyla bir iletişim kanalı oluşturmak için kullanılır.
# OPTIONS: Sunucunun desteklediği HTTP metotlarının bir listesini almak için kullanılır.
# TRACE: Sunucudan gönderilen bir isteğin yolunu takip etmek için kullanılır.

    """


#* ==========================================================
#TODO,         FUNCTION BASED VİEWS
#* ==========================================================


@api_view() #? default GET olarak çalışır.
def students_list(request):
    students = Student.objects.all()
    # print(students)
    serializer = StudentSerializer(students, many=True) #* many=True yazılması gerekiyor, birden çok obje döneceğinden..
    # print(serializer)
    # print(serializer.data)
    return Response(serializer.data)

@api_view(['POST']) #?  POST yapmak için yazdık.
def student_create(request):
    serializer = StudentSerializer(data=request.data) #! many=True yazmıyoruz, TEK obje döneceğinden..
    if serializer.is_valid(): #? Student model de belirlediğimiz field-type lara uygun mu? onu valide ediyor.
        serializer.save()
        message = {
            "message" : f"Student updated succesfully..."
        }
        # return Response(message, status=status.HTTP_201_CREATED) # başarılı giriş yaptıysam 201 versin, ve message çıktısı dönsün
        return Response(serializer.data, status=status.HTTP_201_CREATED) # başarılı giriş yaptıysam 201 versin, ve create edilen data dönsün.
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # kullanıcı yanlış yaparsa 400 hatası versin,

@api_view(['GET'])
def student_detail(request, pk):
    # try:
    #     student = Student.objects.get(id=pk)
    # except:
    #     serializer = StudentSerializer(student) #! many=True yazmıyoruz, TEK obje döneceğinden..
    #     return Response(serializer.data) # http 200 default olduğundan yazmıyoruz.
    

    student = get_object_or_404(Student, id=pk) #? Student içinden yanlış url olursa crash olmasın, 404 hatası versin
    serializer = StudentSerializer(student) #! many=True yazmıyoruz, TEK obje döneceğinden..
    return Response(serializer.data) # http 200 default olduğundan yazmıyoruz.

@api_view(['PUT']) #?  PUT yapmak için yazdık.
def student_update(request, pk):
    student = get_object_or_404(Student, id=pk) #? Student içinden yanlış url olursa crash olmasın, 404 hatası versin
    serializer = StudentSerializer(instance=student, data=request.data) 
    # instance=student, yazıyoruz ki öncesi ile kıyas yapsın, yoksa create eder.
    if serializer.is_valid(): #? Student model de belirlediğimiz field-type lara uygun mu? onu valide ediyor.
        serializer.save()
        message = {
        "message" : f"Student updated succesfully..."
    }
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['DELETE'])
def student_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    message = {
        "message" : f"Student DELETED.."
    }
    return Response(message)


#! ==========================================================
#! pk istemeyenler için bir tane fonksiyon yazıp birleştirilebilir.
#! ==========================================================

@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#! ==========================================================
#! pk, İSTEYENLER için birtane fonksiyon yazıp birleştirilebilir.
#! ==========================================================

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def student_api_get_update_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)

    
#* ==========================================================
#TODO                     CLASS BASED VİEWS
#* ==========================================================


#? ==========================================================
#? APIVIEW 
#? ==========================================================

#! pk istemeyenler için bir tane fonksiyon
class StudentListCreate(APIView):
    
    def get(self, request):  #? fonksiyon ismi get olmak zorunda;
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request): #? fonksiyon ismi post olmak zorunda;
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


#! pk GEREKLİ OLANLAR için bir tane fonksiyon
class StudentDetail(APIView):
    
    def get_obj(self, pk): #? student objesini üretmek için bir metod yazıyoruz;
        return get_object_or_404(Student, id=pk)
    
    def get(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        student = self.get_obj(pk)
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)        

#? ==========================================================
#? GENERIC APIVIEW  -  MIXINS  (ASLINDA KULLANILMIYOR, GEÇİŞİ ANLAMAK İÇİN ANLATILDI)
#? ==========================================================

# One of the key benefits of class-based views is the way they allow you to compose bits of reusable behavior. REST framework takes advantage of this by providing a number of pre-built views that provide for commonly used patterns.

# GenericAPIView class extends REST framework's APIView class, adding commonly required behavior for standard list and detail views.

#? Mixins

""" Mixins
- ListModelMixin
    - list method
- CreateModelMixin
    - create method
- RetrieveModelMixin
    - retrieve method
- UpdateModelMixin
    - update method
- DestroyModelMixin
    - destroy method 
    """
#! pk istemeyenler için bir tane fonksiyon
class StudentGAV(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    
    # GenericAPIView
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # ListModelMixin
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    # CreateModelMixin
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

#! pk GEREKLİ OLANLAR için bir tane fonksiyon    
class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    
    # GenericAPIView
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # RetrieveModelMixin
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)    
    
    # UpdateModelMixin
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
     
    # DestroyModelMixin
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 


#? ==========================================================
#? CONCRETE VIEWS  --  çok sık kullanılan yöntem
#? ==========================================================

#! pk istemeyenler için bir tane fonksiyon
class StudentCV(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
#! pk GEREKLİ OLANLAR için bir tane fonksiyon 
class StudentDetailCV(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#? ==========================================================
#? VIEWSETS
#? ==========================================================
"""
- Django REST framework allows you to combine the logic for a set of related views in a single class, called a ViewSet. 

- Typically, rather than explicitly registering the views in a viewset in the urlconf, you'll register the viewset with a router class, that automatically determines the urlconf for you.

There are two main advantages of using a ViewSet class over using a View class.

 - Repeated logic can be combined into a single class. In the above example, we only need to specify the queryset once, and it'll be used across multiple views.
 - By using routers, we no longer need to deal with wiring up the URL conf ourselves.

Both of these come with a trade-off. Using regular views and URL confs is more explicit and gives you more control. ViewSets are helpful if you want to get up and running quickly, or when you have a large API and you want to enforce a consistent URL configuration throughout.
"""

#! Tek bir view oluşturarak hem pk/id (lookup) gerekli olmayan,(GET, POST)
#! Hem de pk/id (lookup) isteyen bütün bütün işlemleri yapabiliyoruz. (GET, PUT, PATCH, DELETE)

from .pagination import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

#? Permission
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class StudentMVS(ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = CustomPageNumberPagination
    # pagination_class = CustomLimitOffsetPagination
    # pagination_class = CustomCursorPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["id", "first_name", "last_name"]
    search_fields = ["first_name", "last_name"]
    # search_fields=['^first_name']  #baş harfine göre arama yapmak için,
    ordering_fields = ['first_name','last_name']  #* filter boxta hangi seçenekler çıksın istiyorsanız onu yazıyorsunuz
    ordering = ['last_name']  #* default olarak ilk açıldığında buraya yazdığımıza göre sıralıyor
    
    #?permission
    #* herkes CRUD yapabilir
    # permission_classes = [IsAuthenticated]
    
    #* sadece admin olan CRUD yapabilir
    permission_classes = [IsAdminUser]
    
    #* admin olan herşeyi yapar, olmayan sadece GET(read) yapar.
    # permission_classes = [IsAuthenticatedOrReadOnly]
    
    
    
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



# Authentication => bir kişinin ya da bir şeyin iddia ettiği olduğunu doğrulamak için yapılan işlemdir. Bu genellikle bir kullanıcı adı ve parola gibi kimlik bilgileri ya da bir parmak izi veya yüz tanıma gibi biyometrik veriler kullanılarak yapılır.

# Authorization =>  doğrulanmış kullanıcının izinlerine göre belirli kaynaklara veya eylemlere erişimi verme veya reddetme işlemidir. Örneğin, doğrulanmış bir kullanıcının belirli belgeleri okumaya izin verilmiş olabilir, ancak düzenleme veya silme yetkisi olmayabilir.