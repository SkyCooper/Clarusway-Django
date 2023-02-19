from django.shortcuts import render, redirect
from .models import Pizza, Order

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


def my_orders(request):
    
    #? verilen siparişlerden user'ı istek yapan user eşit olan siparişleri bir değişkene atadık,
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders': orders
    }
    return render(request, 'pizzas/my_orders.html', context)


def update_order_view(request, id):
#? sadece belirli bir order update edileceğinden id gerekiyor,
#? order_view'dan farklı olarak form dolu gelecek,

    #? update olacak id'li order alındı
    order = Order.objects.get(id=id)
    
    #? id'si order edilen pizza id'sine eşit olan pizza alındı
    pizza = Pizza.objects.get(id=order.pizza.id)
    
    #? ve son olarak PizzaForm içinde order olacak şekilde dolu olarak çağırıldı,
    form = PizzaForm(instance=order)
    
    if request.method == 'POST':
        
        #? instance=order olmazsa update olmaz, yeniden order create eder.
        form = PizzaForm(request.POST, instance=order)
        if form.is_valid():
            order.save()
            return redirect('my_orders')
    context = {
        'order': order,
        'pizza': pizza,
        "form" : form
    }
    return render(request, 'pizzas/update_order.html', context)

def delete_order_view(request, id):
#? ilave bir template tanımlamaya gerek yok, işlemi yapacak ve tekrar sipariş sayfasına dönecek
    order = Order.objects.get(id=id)
    order.delete()
    return redirect('my_orders')