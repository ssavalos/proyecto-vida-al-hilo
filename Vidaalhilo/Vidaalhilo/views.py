from django.template import loader 
from django.shortcuts import render 
def home(request):
    return render(request, 'home.html')
