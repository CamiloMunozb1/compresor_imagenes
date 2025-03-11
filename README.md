## Compresor de Imágenes con Python (Pillow)

Este es un pequeño script de automatización que permite convertir imágenes a formato JPEG y reducir su calidad para disminuir el tamaño del archivo. Se ha diseñado con el propósito de ser rápido y eficiente, sin necesidad de interfaces gráficas innecesarias.

## Características

✔ Convierte imágenes a JPEG en formato RGB.

✔ Comprime las imágenes reduciendo su calidad (60% por defecto).

✔ Captura errores para evitar interrupciones inesperadas.

✔ No usa interfaces gráficas, ya que es un script de automatización.

## Requisitos

Asegúrate de tener instalada la librería Pillow antes de ejecutar el script. Puedes instalarla con:

    pip install pillow
  
## Uso

Ejecuta el script en la terminal o línea de comandos y sigue las instrucciones:

    python compresor.py
  
Al ejecutarlo, te pedirá ingresar la ruta de la imagen. Luego, guardará una nueva imagen comprimida en el mismo directorio con el nombre nueva_imagen.jpg.

## Notas

La compresión predeterminada es del 60%, pero puedes modificar este valor en el código.
Si necesitas procesar varias imágenes, puedes adaptar el script para hacerlo en un bucle.
Este script está pensado para automatización, por lo que no incluye una interfaz gráfica.


 Autor: Juan camilo Muñoz Bautista
 
 Última actualización: 10/03/25
