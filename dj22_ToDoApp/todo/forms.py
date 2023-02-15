from django import forms
#? serializer yerine forms import ediyoruz,

from .models import Todo
#? kullanacağımız modeli import ediyoruz.

#? forms içinde Form ve ModelForm var, %99 ModelForm kullanılır.
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        #? post yani create yapılacağı zaman gerekli alanları yazıyoruz, veya hepsi deyip geçiyoruz.
        #? gelen data'lardan hesaplanıp DB'ye aktarılan bir field varsa onu çıkarmak gerekir.
        # fields = '__all__'
        exclude = []


#* https://docs.djangoproject.com/en/4.1/topics/forms/
#! burada önemli bir özellik Django Form validasyonu kendisi yapıyor,
# yani bu örnek için konuşursak fist_name girmek zorunlu ve max 50 karakter geçemez,
# number alanı sadece sayı girilebilir vs.
# bu validasyonları Django kendisi yapıyor.
# buna bakmak için http://127.0.0.1:8000/add/ bu adreste inspect yaparsak,
# form yapısı ve her input'un özellikleri görünür.