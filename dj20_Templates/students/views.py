from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(resquest):
#     return HttpResponse("<h1> Hello FS-12</h1>")


#* https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#
#? DTL ile yapılması;
def home(resquest):
    
    context = {
        'title' : 'cooper',
        'desc' : 'this is description',
        'number' : 4285,
        'list' : ['a', 1, ['b', 'c', 33], "ali"],
        'dict' : {
            'key1' : 'value1',
            'key2' : 2222,
        },
        'dict_list' : [
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
    {'name': 'zed', 'age': 19},
],
        
    }
    # return render(resquest, 'home.html', context)
    return render(resquest, 'students/home.html', context)


'''
{{ variables }}
{% command %}
| --> filter
'''
