from django import forms
from django.forms import ModelForm
from .models import USER

#Los formularios permiten crear datos a partir de una tabla creada en models

class UserForm(ModelForm):
    class Meta:
        model = USER
        fields = ['username', 'email', 'password']
        
        
        """widget = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.Select(attrs={'form-control'}),           
        } """