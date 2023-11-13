from django.urls import path
from installed_apps import views

urlpatterns = [
    path('',views.General_Pagina),
    path('videos/',views.Videos_Pagina),
    path('buscador/',views.Buscador),
    path('contacto/',views.Contacto),
    path('Login/',views.Login),
    path('registrarse/',views.registrarse),
    path('homekaty/',views.homekaty),
    path('comofuncionamos/',views.comofuncionamos),
    path('tutoriales/',views.tutoriales)

]