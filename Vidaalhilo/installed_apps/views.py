from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from installed_apps.catalogo.helpers import concatenar_imagenes
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import RegisterForm
import io
from .form import User
from PIL import Image
import base64
import os
from django.contrib.auth.decorators import login_required
from .form import FotoForm
from .models import Foto
from .models import Publicacion
from itertools import groupby
from django.db.models import Q
from django.contrib.auth import logout

def ver_perfil(request, usuario_id):
    usuario = User.objects.get(id=usuario_id)  # Recupera el usuario desde la base de datos
    return render(request, 'perfil.html', {'user': usuario})  # Renderiza la plantilla con los datos del usuario

def General_Pagina(request):
    return render(request, "installed_apps/Home.html")

def Videos_Pagina(request):
    return render(request, "installed_apps/Videos.html")
def Buscador(request):
    return render(request, "installed_apps/Buscador.html")

def mis_publicaciones(request):
    mis_publicaciones = Foto.objects.filter(usuario=request.user)
    return render(request, "installed_apps/MisPublicaciones.html", {'mis_publicaciones': mis_publicaciones})

#Buscador que si funciona
def buscar_fotos(request):
    if request.method == "GET":
        query = request.GET.get("q")
        fotos = Foto.objects.filter(descripcion__icontains=query)
        return render(request, 'installed_apps/buscar_fotos.html', {'fotos': fotos, 'query': query})
    else:
        # Maneja otros métodos HTTP según sea necesario
        return HttpResponse("Método no permitido")

#Menu opciones
def mostrar_fotos_mujeres(request):
    fotos_mujeres = Foto.objects.filter(genero='mujer')
    return render(request, 'installed_apps/mujeres.html', {'fotos_mujeres': fotos_mujeres})

def mostrar_fotos_hombres(request):
    fotos_hombres = Foto.objects.filter(genero='hombre')
    return render(request, 'installed_apps/hombres.html', {'fotos_hombres': fotos_hombres})

def mostrar_fotos_ninos(request):
    fotos_ninos = Foto.objects.filter(genero='niño')
    return render(request, 'installed_apps/niños.html', {'fotos_ninos': fotos_ninos})


def Contacto(request):
    if request.method == "POST":
        subject = request.POST["asunto"]

        message = request.POST["mensaje"] + " " + request.POST["email"]

        email_from = settings.EMAIL_HOST_USER

        recipient_list = ["cristobalfr23@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, "installed_apps/Gracias.html")
    return render(request, "installed_apps/Contacto.html")

def registrarse(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/homekaty")
        return render(request, "registration/register.html", {"form": form})
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})


def homekaty(request):
    fotos = Foto.objects.all().order_by('id', 'categoria')
    grouped_photos = {categoria: list(g) for categoria, g in groupby(fotos, key=lambda x: x.categoria)}
    return render(request, "installed_apps/homekaty.html", {'grouped_photos': grouped_photos})


def mujeres(request):
    return render(request, "installed_apps/mujeres.html")
def hombres(request):
    return render(request, "installed_apps/hombres.html")
def niños(request):
    return render(request, "installed_apps/niños.html")
def comofuncionamos(request):
    return render(request, "installed_apps/comofuncionamos.html")
def tutoriales(request):
    return render(request, "installed_apps/tutoriales.html")
def olvidastelacontraseña(request):
    return render(request, "installed_apps/olvidastelacontraseña.html")
def perfil(request):
    return render(request, "installed_apps/perfil.html")
def concatenar_fotos(request):
    if request.method == "POST":
        # Obtén las rutas de las imágenes desde el formulario
        prenda1_path = request.FILES.get("prenda1")
        prenda2_path = request.FILES.get("prenda2")

        # Lógica para concatenar las imágenes (debes implementar esta función)
        try:
            imagen_final = concatenar_imagenes(prenda1_path, prenda2_path)
        except Exception as e:
            return HttpResponse(f"Error: {e}")

        # Guarda la imagen en un objeto BytesIO
        output = io.BytesIO()
        imagen_final.save(output, format="PNG")
        contents = output.getvalue()
        output.close()

        # Codifica la imagen en base64
        imagen_base64 = base64.b64encode(contents).decode('utf-8')

        # Renderiza la plantilla con la imagen concatenada
        return render(request, 'installed_apps/homekaty.html', {'imagen_final': imagen_base64})
    else:
        # Maneja el caso cuando el método no es POST
        return HttpResponse("Método no permitido")
    
@login_required
def publicar_foto(request):
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            foto = form.save(commit=False)
            foto.usuario = request.user
            foto.save()
            return redirect('listar_fotos')  # Ajusta esto a la vista que muestra la lista de fotos
    else:
        form = FotoForm()

    return render(request, 'installed_apps/publicar_foto.html', {'form': form})


def listar_fotos(request):
    fotos = Foto.objects.all()
    return render(request, 'installed_apps/listar_fotos.html', {'fotos': fotos})

def eliminar_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, pk=publicacion_id)
    
    if request.method == 'POST':
        publicacion.delete()
        return redirect('listar_publicaciones')

    return render(request, 'installed_apps/eliminar_publicacion.html', {'publicacion': publicacion})

def cerrar_sesion(request):
    logout(request)
    # Redirigir a la página de inicio o a otra página deseada
    return redirect('installed_apps/login.html')