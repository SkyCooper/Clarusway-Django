from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        #? post yani create yapılacağı için gerekli alanları yazıyoruz, veya hepsi deyip geçiyoruz.
        fields = '__all__'
