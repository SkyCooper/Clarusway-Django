from django.shortcuts import render
from django.http import HttpResponse

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
