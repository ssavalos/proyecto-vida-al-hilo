from django.urls import path
from installed_apps import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('',views.General_Pagina),
    path('videos/',views.Videos_Pagina),
    path('buscador/',views.Buscador),
    path('contacto/',views.Contacto),
    path('admin/', admin.site.urls),
    path('registrarse/', views.registrarse, name="registro"),
    path('homekaty/',views.homekaty),
    path('comofuncionamos/',views.comofuncionamos),
    path('tutoriales/',views.tutoriales),
    path('olvidastelacontraseña/',views.olvidastelacontraseña),
    path('perfil/',views.perfil),

]