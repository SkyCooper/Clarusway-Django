from django.shortcuts import render,redirect

#? djangonun default user creation formu
from django.contrib.auth.forms import UserCreationForm

#? djangonun default user creation formu
from django.contrib.auth.forms import AuthenticationForm

#? djangonun default login/logout fonksiyonu
from django.contrib.auth import login, logout

from .forms import UserForm, LoginForm

# Create your views here.

def register(request):
    # form = UserCreationForm()
    form = UserForm()
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # form sayfasında kalmasın, save olduktan sonra başka yere yönlendirilsin;
            return redirect("home")
    
    context = {
        "form" : form
    }
    
    return render(request,'users/register.html', context)


def user_login(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    
    
    context = {
        "form" : form
    }
    return render(request,'users/login.html', context)

def user_logout(request):
    logout(request)
    return redirect("home")