from django.shortcuts import render,redirect

#? 1-djangonun default user creation formu (register işlemleri için)
from django.contrib.auth.forms import UserCreationForm
#? 2-UserCreationForm inherit edilerek yeni bir form ile yapma
from .forms import UserForm

#? 1-djangonun default user Authentication formu
from django.contrib.auth.forms import AuthenticationForm
#? 2-AuthenticationForm inherit edilerek yeni bir form ile yapma
from .forms import LoginForm


#? djangonun default login/logout fonksiyonu
from django.contrib.auth import login, logout

#? djangonun default user creation formu
from django.contrib import messages


# Create your views here.

def register(request):
#* A-yapılan istek get ise form boş olarak gelsin
    
    #? 1-default UserCreationForm ile yapma;
    # form = UserCreationForm()
    
    #? 2- UserCreationForm inherit edilerek yeni bir form ile yapma;
    form = UserForm()
    
    #* B-yapılan istek post ise, form içine yazılan bilgilerle bir user create etsin
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserForm(request.POST)
        
        if form.is_valid():
            # form.save()
            
            user = form.save()
            login(request, user)
            
            # username = form.cleaned_data.get("username")
            # password = form.cleaned_data.get("password2")
            # user = authenticate(username=username, password=password)
            # login(request, user)        
            
            
            #? form sayfasında kalmasın, save olduktan sonra başka yere yönlendirilsin;
            return redirect("home")
    
    context = {
        "form" : form
    }
    
    return render(request,'users/register.html', context)




def user_login(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        
    context = {
        "form": form
    }
    return render(request,'users/login.html', context)

def user_logout(request):
    logout(request)
    messages.success(request, 'Succesfully loged out')
    return redirect("home")