from django.shortcuts import render, redirect
from .models import Pizza

from .forms import PizzaForm

# Create your views here.

#? django bir template ararken app'lerin altındaki templates klasörlerine bakıyor,
#? bunun için app içindeki klasör isminin templates olması ZORUNLU
#? "pizzas/home.html" bunu yazınca bu view bulunduğu app içindeki templates klasörüne bakıyor,
#? yani ; pizzas/templates/pizzas/home.html

def home(requset):
    return render(requset, "pizzas/home.html")


def pizzas(request):
    #? bütün pizza objelerini DB'den çekip pizzas değişkenine atadık,'
    pizzas = Pizza.objects.all()
    
    #? context yapısı ile paketleyip, pizzas.html templatenine gönderdik.
    context = {
        'pizzas': pizzas
    }
    return render(request, 'pizzas/pizzas.html', context)


def order_view(request, id):
    #? id ile geldiğinden id'si gelen id'ye eşit olan pizzayı çekebilirim,
    pizza = Pizza.objects.get(id=id)
    
    #? post yapılmışsa içine gelen veriyi koy, get ise boş olarak getir
    form = PizzaForm(request.POST or None)
    
    #? eğer post yapıomış ise ve form valid ise;
    if request.method == 'POST':
        if form.is_valid():
            
            #! commit=False sayesinde DB'de obje create edilmez fakat oluşmuş olur ve değişkene atayabilirim
            #! böylece üzerinde değişiklik yapılabilir, forms.py da eklenmeyen pizza ve user sonradan eklenebilir.
            order = form.save(commit=False)
            
            #? siparişe pizzayı ekle
            order.pizza = pizza
            
            #? siparişe user ekle
            order.user = request.user
            
            #? kayıt et ve siparişlerim sayfasına yönlendir.
            order.save()
            return redirect('my_orders')            
    
    context = {
        'pizza': pizza,
        'form': form
    }
    return render(request, 'pizzas/order.html', context)