from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=8)

class Articulo(models.Model):
    nombre= models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

class Pedido(models.Model):
    numero= models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

class Seccion(models.Model):
    nombre = models.CharField(max_length=100)

class Foto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='fotos/')
    descripcion = models.TextField()
    categoria = models.CharField(max_length=20, choices=[('superior', 'Parte superior'), ('inferior', 'Parte inferior')], default='superior')
    genero = models.CharField(max_length=10, choices=[('mujer', 'Mujer'), ('hombre', 'Hombre'), ('niño', 'Niño')], default='mujer')

    def __str__(self):
        return self.descripcion
    
    
class Publicacion(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo