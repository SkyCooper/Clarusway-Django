from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
#! pk, isteyenler için birtane istemeyenler için bir tane fonksiyon yazıp birleştirilebilir.
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























