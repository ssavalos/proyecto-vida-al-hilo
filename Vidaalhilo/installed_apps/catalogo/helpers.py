from PIL import Image
from django.shortcuts import render
from django.http import HttpResponse
import os

def concatenar_imagenes(prenda1, prenda2):
    try:
        im1 = Image.open(prenda1)
        im2 = Image.open(prenda2)
    except Exception as e:
        raise Exception(f"Error al abrir las imágenes: {e}")

    # Asegurarse de que ambas imágenes sean del mismo modo de color y canal
    im1 = im1.convert('RGB')
    im2 = im2.convert('RGB')

    # Ajustar el tamaño de la segunda imagen para que coincida con el ancho de la primera
    im2 = im2.resize((im1.width, im2.height))

    # Crear una nueva imagen con la altura combinada
    imagen_concatenada = Image.new('RGB', (im1.width, im1.height + im2.height))

    # Pegar las dos imágenes en la nueva imagen
    imagen_concatenada.paste(im1, (0, 0))
    imagen_concatenada.paste(im2, (0, im1.height))

    return imagen_concatenada