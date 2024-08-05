from django import forms

from cliente.models import Cliente, Servicos  

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ()
        
       
        
        
        