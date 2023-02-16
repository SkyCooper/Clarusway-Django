from django.contrib.auth.forms import UserCreationForm
#? djangonun default user creation formu

from django.contrib.auth.models import User
#? kullanacağımız modeli import ediyoruz.

from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UsernameField


#? forms import etmeden UserCreationForm'dan inherit ederek form oluşturuyoruz.
class UserForm(UserCreationForm):
    
    # class Meta:
    #     model = User
    #     fields = ("username", "email", "password1", "password2" )


    username = UsernameField(
        label=(""),
        widget=forms.TextInput(attrs={"autofocus": True,'class' : "rounded border border-warning form-control shadow-lg m-2", "placeHolder" :"username"})
        )
    
    password1 = forms.CharField(
        label=(""),
        widget=forms.PasswordInput(attrs={'class' : "rounded border border-warning form-control shadow-lg m-2", "placeHolder" :"password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    
    password2 = forms.CharField(
        label=(""),
        widget=forms.PasswordInput(attrs={'class' : "rounded border border-warning form-control shadow-lg m-2", "placeHolder" :"Password confirmation"}),
        help_text=("* Enter the same password as before, for verification."),
    )




#* https://docs.djangoproject.com/en/4.1/topics/forms/
#! burada önemli bir özellik Django Form validasyonu kendisi yapıyor,
# yani bu örnek için konuşursak fist_name girmek zorunlu ve max 50 karakter geçemez,
# number alanı sadece sayı girilebilir vs.
# bu validasyonları Django kendisi yapıyor.
# buna bakmak için http://127.0.0.1:8000/add/ bu adreste inspect yaparsak,
# form yapısı ve her input'un özellikleri görünür.