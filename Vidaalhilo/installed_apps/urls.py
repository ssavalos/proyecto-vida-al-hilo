from django.urls import path
from installed_apps import views

urlpatterns = [
    path('',views.General_Pagina),
    path('videos/',views.Videos_Pagina),
    path('buscador/',views.Buscador),
    path('contacto/',views.Contacto),
    path('login/',views.Login),
]