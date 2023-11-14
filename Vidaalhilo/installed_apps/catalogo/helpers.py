from PIL import Image

def concatenar_imagenes(im1, im2):
    dst = Image.new('RGB', (min(im1.width, im2.width), im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst
