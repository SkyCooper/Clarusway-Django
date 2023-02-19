from django import forms
from .models import Order


class PizzaForm(forms.ModelForm):
    
    class Meta:
        model = Order
        
        #? pizza modelinde var olan pizza fieldını seçili pizzadan ekledik,
        #? user fieldını istek yapan user'dan ekledik
        fields = (
            'size',
            'quantity',
        )
        
        #? size için radioselect kullandık
        #? quantity için TextInput kullandık
        widgets = {
            'size':forms.RadioSelect,
            'quantity': forms.TextInput(attrs={'class' : "rounded border border-warning form-control", "style" : "width: 50%;"}),          
        }