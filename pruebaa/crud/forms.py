from django import forms
from .models import Persona, Rol

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'email', 'rol', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
        }

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nombre']

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)