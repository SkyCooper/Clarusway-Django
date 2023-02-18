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
#* A-yapılan istek get ise form boş olarak gelsin
    #? 1-default AuthenticationForm ile yapma;
    # form = AuthenticationForm()
    
    #? 2- AuthenticationForm inherit edilerek yeni bir form ile yapma;
    form = LoginForm()

    #* B-yapılan istek post ise, form içine yazılan bilgilerle user login olsun,
    if request.method == 'POST':
        # form = AuthenticationForm(request, data=request.POST)
        
        #? herzaman request.POST yazıyorduk, burada onu FARKLI yazdık.
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            
            #? formun içinden get_user() metodu ile user çekip bir değişkene atadık,
            user = form.get_user()
            
            #? djangonun default login fonksiyonuna yukarıda yakaladığımız user'ı ekliyoruz
            login(request, user)
            
            #? başarılı bir login işlemi olduysa mesaj versin
            messages.success(request, 'You are now logged in')
            
            #? işlem tamamlanınca home sayfasına gitsin
            return redirect('home')
        
    context = {
        "form": form
    }
    return render(request,'users/login.html', context)



#? logout olduğunda ilave bir template render etmesine gerek yok,
#? işlemi yapsın ve home sayfasına gitsin,
def user_logout(request):
    #? djangonun default logout fonksiyonu gelen isteğe göre işlemleri arka planda yapıyor.
    logout(request)
    
    #? başarılı ise mesaj yazdırıyor,
    messages.success(request, 'Succesfully loged out')
    
    #? ve home sayfasına gidiyor,
    return redirect("home")