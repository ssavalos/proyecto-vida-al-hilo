# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Foto

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class FotoForm(forms.ModelForm):
    telefono = forms.CharField(max_length=12, required=False)  # Nuevo campo para el número de teléfono

    class Meta:
        model = Foto
        fields = ['imagen', 'descripcion', 'categoria', 'genero', 'telefono']  # Agrega 'telefono' al formulario
