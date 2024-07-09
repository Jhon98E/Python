"""
Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
    --> URL de Ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
    --> Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen 1920*1080px.
"""


import requests
from PIL import Image
from io import BytesIO
import math

def calcular_aspect_ratio(ancho, alto):
    # Encontrar el máximo común divisor (MCD)
    mcd = math.gcd(ancho, alto)
    
    # Dividir el ancho y el alto por el MCD para simplificar la fracción
    aspect_ratio_ancho = ancho // mcd
    aspect_ratio_alto = alto // mcd
    
    return (aspect_ratio_ancho, aspect_ratio_alto)

def obtener_dimensiones_imagen(url):
    # Descargar la imagen desde la URL
    response = requests.get(url)
    response.raise_for_status()  # Verificar si la solicitud fue exitosa
    
    # Abrir la imagen usando Pillow
    image = Image.open(BytesIO(response.content))
    
    # Obtener las dimensiones de la imagen
    ancho, alto = image.size
    
    return ancho, alto

def main():
    url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
    ancho, alto = obtener_dimensiones_imagen(url)
    
    aspect_ratio = calcular_aspect_ratio(ancho, alto)
    print(f"Las dimensiones de la imagen son: {ancho}x{alto} píxeles")
    print(f"El aspect ratio es: {aspect_ratio[0]}:{aspect_ratio[1]}")

if __name__ == "__main__":
    main()


