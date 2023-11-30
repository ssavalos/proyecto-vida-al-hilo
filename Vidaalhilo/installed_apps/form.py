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
    class Meta:
        model = Foto
        fields = ['imagen', 'descripcion', 'categoria', 'genero']