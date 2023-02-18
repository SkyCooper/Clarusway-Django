from django.shortcuts import render
from .models import Pizza

# Create your views here.

#? django bir template ararken app'lerin altındaki templates klasörlerine bakıyor,
#? bunun için app içindeki klasör isminin templates olması ZORUNLU
#? "pizzas/home.html" bunu yazınca bu view bulunduğu app içindeki templates klasörüne bakıyor,
#? yani ; pizzas/templates/pizzas/home.html

def home(requset):
    return render(requset, "pizzas/home.html")


def pizzas(request):
    pizzas = Pizza.objects.all()
    
    context = {
        "pizzas" : pizzas
    }
    
    return render(request, 'pizzas/pizzas.html', context)