# Importamos la librería Pillow (PIL) para trabajar con imágenes
from PIL import Image

try:
    # Pedimos al usuario que ingrese la ruta de la imagen
    imagen_usuario = str(input("Ingresa la direccion de la imagen: "))

    # Abrimos la imagen usando Image.open()
    imagen_abierta = Image.open(imagen_usuario)

    # Convertimos la imagen a formato RGB (esto es útil si la imagen original está en otro modo, como CMYK o RGBA)
    imagen_convertida = imagen_abierta.convert("RGB")

    # Guardamos la nueva imagen en formato JPEG con una calidad del 60%
    imagen_convertida.save("nueva_imagen.jpg", "JPEG", quality=60)

except Exception as error:
    # Capturamos cualquier error y lo mostramos en pantalla
    print(f"Error en el programa: {error}.")
