from django.urls import path
from installed_apps import views
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView
from .views import cerrar_sesion


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
    path('listar_fotos/', views.listar_fotos, name='listar_fotos'),
    path('publicacion/<int:publicacion_id>/eliminar/', views.eliminar_publicacion, name='eliminar_publicacion'),
    path('buscar/', views.buscar_fotos, name='buscar_fotos'),
    path('mujeres/', views.mostrar_fotos_mujeres, name='mostrar_fotos_mujeres'),
    path('hombres/', views.mostrar_fotos_hombres, name='mostrar_fotos_hombres'),
    path('ninos/', views.mostrar_fotos_ninos, name='mostrar_fotos_ninos'),
    path('cerrar_sesion/', LogoutView.as_view(), name='cerrar_sesion'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)