from django.db import models

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