from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import User

def ver_perfil(request, usuario_id):
    usuario = User.objects.get(id=usuario_id)  # Recupera el usuario desde la base de datos
    return render(request, 'perfil.html', {'user': usuario})  # Renderiza la plantilla con los datos del usuario

def General_Pagina(request):
    return render(request, 'installed_apps/Home.html')
def Videos_Pagina(request):
    return render(request, 'installed_apps/Videos.html')
def Buscador(request):
    return render(request, 'installed_apps/Buscador.html')
def Contacto(request):
    if request.method=="POST":
        subject=request.POST['asunto']

        message=request.POST["mensaje"] + " " + request.POST['email']

        email_from=settings.EMAIL_HOST_USER

        recipient_list=['cristobalfr23@gmail.com']

        send_mail(subject, message, email_from, recipient_list)


        return render(request, 'installed_apps/Gracias.html')
    return render(request, 'installed_apps/Contacto.html')
def Login(request):
    return render(request, 'installed_apps/Login.html')
def registrarse(request):
    return render(request, 'installed_apps/registrarse.html')
def homekaty(request):
    return render(request, 'installed_apps/homekaty.html')
def comofuncionamos(request):
    return render(request, 'installed_apps/comofuncionamos.html')
def tutoriales(request):
    return render(request, 'installed_apps/tutoriales.html')
def olvidastelacontraseña(request):
    return render(request, 'installed_apps/olvidastelacontraseña.html')
def perfil(request):
    return render(request, 'installed_apps/perfil.html')
    