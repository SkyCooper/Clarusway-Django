from django.shortcuts import render
from django.http import HttpResponse

#todo, form dersi importları
#? modeli import ediyoruz
from .models import Student

#? forms.py içinde oluşturduğumuz Form import ediliyor.
from .forms import StudentForm

#? yönlendirme yapmak için
from django.shortcuts import redirect

from django.shortcuts import get_object_or_404


# Create your views here.

# def home(resquest):
#     return HttpResponse("<h1> Hello FS-12</h1>")


#? DTL ile yapılması;
def home(resquest):
    
    context = {
        'title' : 'cooper',
        'desc' : 'this is description',
        'number' : 4285,
        
        'list' : ['a', 1, ['b', 'c', 33], "ali"],
        
        'dict' : {
            'key1' : 'value1',
            'key2' : 2222
                },
        
        'dict_list' : [
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
            {'name': 'zed', 'age': 19},
                        ]
        }
    
    #? render fonksiyonu aldığı parametreler;
    #* def render(request, template_name, context=None, content_type=None, status=None, using=None)
    # request yani bir istek geldi, 
    # template_name, bu istek gelince hangi template çalışacak,
    # context, ismi değişebilir, template içine değişken aktarmak için key/value şeklinde tanımlanıyor.
    # content_type, status, using, bunlar çok kullanılmıyor, örnek yapılmadı.
    
    #? root'da bulunan templates klasörü içindeki home.html çalışır,
    # return render(resquest, 'home.html', context)

    #? students içinde bulunan templates klasörü içindeki home.html çalışır,
    # return render(resquest, 'students/home.html', context)

    #? students içinde bulunan templates klasörü içindeki index.html (root base.html'den inherit edilen) çalışır,
    return render(resquest, 'students/index.html', context)


'''
{{ variables }}
değişkenler çift süslü içine yazılır,
başında ve sonunda boşluk bırakılırsa daha iyi olur, bazen hata verebiliyor.
view'da context adı ile, dictionary formatında tanımlanan değişkenin key'ine karşılık gelen value'yi temsil eder,
{{ title }} --> cooper



{% tags %}
[Tags reference](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#ref-templates-builtins-tags)

komutlar açılış/kapanış blokları halinde yazılır,

{% block title %}
Index Home
{% endblock title %}

{% for i in list %}
<li>{{ i }}</li>
{% endfor %}




| -- filter
[Filters reference](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#ref-templates-builtins-filters)

filitreleme için pipe işareti ( | ) kullanılır,
{{ context'ten alınan değişken | yapılacak filitreleme işlemi }}
filter işlemi sadece çıktıyı etkiler, esas değer değişmez

number key'in valuesine 15 ekle, {{ number | add:'15' }}    = 4285+15 ,4300
esas/orjinal value {{ number }}                             = 4285, değişmedi

içinde listeler olan dicti age'e göre sırala; {{ dict_list|dictsort:"age" }}

desc valuesinin ilk 7 karakterini göster ;{{ desc|truncatechars:7 }}
'''

#! Django form işlemleri;
# önce bir model oluşturup, sonra bu modeli admin panele tanıtıp, admin panelden birkaç tane öğrenci ekledik.
# daha sonra CRUD işlemleri için function-based view'lar yazdık.
# genel bir mantık olarak bütün hepsinde context tanımlayıp,
# return render(request, "students/student_list.html", context) bunu yazıyoruz.
# yazılan her view için root içindeki base.html'den inherit ederek app içinde aynı isimli bir html dosyası oluşturduk,
# her view için app/urls içinde bir path tanımladık,

#* öğrencileri listelemek/görüntülemek için,
def student_list(request):
    #? bütün öğrencileri görüntüleyebilmek için
    #? Student modeldeki bütün objeleri alıp değişkene atadık,
    students = Student.objects.all()
    #? gelen data bir queryset'tir.
    
    #? bu student değişkeni context içinde value olacak şekilde yeniden tanımladık,
    context = {
        "students" : students
    }
    
    #? ve context içindeki herşeyi kullanabilmek için student_list.html içine aktardık.
    return render(request, "students/student_list.html", context)



#* yeni bir öğrenci oluşturmak/create etmek için;
#? burada serializer görevine yapacak form yapısını kullanıyoruz,
#? app içinde forms.py isimli bir dosya oluşturuyoruz.
def student_add(request):
    # 1-context içine form'dan gelen data'yı koymak için onu bir değişkene atıyoruz,
    form = StudentForm()
    
    if request.method == 'POST':
        
        #? request.POST ile forma girilen dataları yakalayabiliyoruz,
        print("POST :", request.POST)
        # POST : <QueryDict: {'csrfmiddlewaretoken': ['HlpQpP1ZcxD4gBSlLHo2oDAKSOY2jsVqSFeRSneCrQwWbAaRQ2TOkkAibvm7V8GB'], 'first_name': ['Kahramanmaraş'], 'last_name': ['DEPREMİ'], 'number': ['06022023'], 'image': ['']}>
        
        #? aslında image yukarıda var fakat daha kolay ulaşmak için; 
        print("FILES :", request.FILES)
        # FILES : <MultiValueDict: {'image': [<InMemoryUploadedFile: avatar-tie.png (image/png)>]}>
        
        # 2-data boş gitmemesi için içine, yukarıda örnek çıktıları verilen dataları ekliyoruz.
        form = StudentForm(request.POST, request.FILES)
        
        # eğer gelen datalar uygunsa kayıt et.
        if form.is_valid():
            form.save()
            
            #? artık form sayfasında kalmasın, save olduktan sonra başka yere yönlendirilsin;
            #? redirect için url tarafında belittiğimiz ismi yazmak daha kullanışlı redirect("name")
            #? urls.py içinde name ile ilgili açıklama notu var.
            return redirect("student_list") # name ile yazılması
            # return redirect("/list") # path ile yazılması
    
    # 3-değişkene atanan StudentForm()'u kullanabilmek için context içine value olarak atıyoruz,
    context = {
        "form" : form
    }
    
    return render(request, "students/student_add.html", context)


#* var olan bir öğrenciyi güncellemek/update etmek için;
#? tek bir öğrenci update edileceği için id kullanmak gerekli,
# yukarıdaki create/add ile çok benzer, sadece instance=student eklemek gerekiyor.
def student_update(request, id):
    
    # get_object_or_404, eğer update edilmek istenen öğrenci yoksa (mesela id:315 yok)
    # crush olmadan 404 hatsaı versin diye kullanıyoruz,
    #? hangi öğrenci update edilecek,(id'si benim yazdığım id ile eşleşen)
    student = get_object_or_404(Student, id=id)
    
    #? form boş olarak gelmesin, yukarıdaki obje bilgileri ile gelsin;
    # 1-bunu bir değişkene atıyoruz
    form = StudentForm(instance=student)
    
    if request.method == 'POST':
        # 2-data boş gitmemesi için içine verileri ekliyoruz,
        # instance=student bunu eklemezsek yeni bir öğrenci create eder,
        # ekleyince değikliğe göre update ediyor.
        form = StudentForm(request.POST, request.FILES, instance=student)
        
        # form uygunsa kayıt et
        if form.is_valid():
            form.save()
            
            # form sayfasında kalmasın, save olduktan sonra başka yere yönlendirilsin;
            return redirect("student_list")
    
    context = {
        "form" : form
    }
    
    return render(request, "students/student_update.html", context)


def student_detail(request, id):
    student = get_object_or_404(Student, id=id)

    context = {
        "student" : student
    }
    
    return render(request, "students/student_detail.html", context)


def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == 'POST':
        student.delete()
            
        #? artık form sayfasında kalmasın, save olduktan sonra başka yere yönlendirilsin;
        #? redirect için url tarafında belittiğimiz ismi yazmak daha mantıklı redirect("name")
        return redirect("student_list")
        # return redirect("/list") # path ile yazılması

    context = {
        "student" : student
    }
    
    return render(request, "students/student_delete.html", context)

