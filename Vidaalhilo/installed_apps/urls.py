from django.urls import path
from installed_apps import views
from django.contrib import admin
from django.urls import path, include 
from .views import publicar_foto, listar_fotos



urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('',views.General_Pagina),
    path('registrarse/', views.registrarse, name="registro"),
    path('videos/',views.Videos_Pagina),
    path('buscador/',views.Buscador),
    path('contacto/',views.Contacto),
    path('homekaty/',views.homekaty),
    path('comofuncionamos/',views.comofuncionamos),
    path('tutoriales/',views.tutoriales),
    path('olvidastelacontraseña/',views.olvidastelacontraseña),
    path('perfil/',views.perfil),
    path('concatenar/', views.concatenar_fotos, name='concatenar_fotos'),
    path('publicar_foto/', views.publicar_foto, name='publicar_foto'),
    path('listar_fotos/', views.listar_fotos, name='listar_fotos')

]