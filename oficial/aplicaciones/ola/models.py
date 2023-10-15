from django.db import models

# Create myour models here.
class curso(models.Model):
    nombre=models.CharField(max_length=30)
    creditos=models.PositiveSmallIntegerField()
    