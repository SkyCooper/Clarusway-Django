from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

from .forms import StudentForm
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


def student_list(request):
    #? Student modeldeki bütün objeleri alıp değişkene atadık,
    students = Student.objects.all()
    
    #? bu student değişkeni value olacak şekilde yeniden tanımladık,
    context = {
        "students" : students
    }
    
    return render(request, "students/student_list.html", context)


def student_add(request):
    form = StudentForm()
    
    if request.method == 'POST':
        # print("POST :", request.POST)
        # print("FILES :", request.FILES)
        
        form = StudentForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            
            #? artık form sayfasında kalmasın, save olduktan sonra başka yere yönlendirilsin;
            #? redirect için url tarafında belittiğimiz ismi yazmak daha mantıklı redirect("name")
            return redirect("student_list")
            # return redirect("/list") # path ile yazılması
    
    context = {
        "form" : form
    }
    
    return render(request, "students/student_add.html", context)


def student_update(request, id):
    # student = Student.objects.all()
    student = get_object_or_404(Student, id=id)
    
    #? formu yukarıdaki obje ile doldurmak için;
    form = StudentForm(instance=student)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            
            #? artık form sayfasında kalmasın, save olduktan sonra başka yere yönlendirilsin;
            #? redirect için url tarafında belittiğimiz ismi yazmak daha mantıklı redirect("name")
            return redirect("student_list")
            # return redirect("/list") # path ile yazılması
    
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

