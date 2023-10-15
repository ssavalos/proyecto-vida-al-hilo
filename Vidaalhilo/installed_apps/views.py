from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

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