"""
Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
    --> Los signos de puntuación no forman parte de la palabra.
    --> Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
    --> No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""

def contar_palabras(texto:str):
    """Cuenta la frecuencia de cada palabra en un texto dado.

    Args:
        texto: El texto a analizar.

    Returns:
        Un diccionario donde las claves son las palabras y los valores son sus frecuencias.
    """

    # Convertir el texto a minúsculas y dividirlo en palabras
    palabras = texto.lower().split()
    
    # Crear un diccionario para almacenar las frecuencias
    conteo_palabras = {}

    # Iterar sobre cada palabra
    for palabra in palabras:
        palabra_limpia = "".join(caracter for caracter in palabra if caracter.isalnum())
        
        # Si l apalabra limpia ya existe en el diccionario, aumentaremos la cuenta para esa palabra
        if palabra_limpia in conteo_palabras:
            conteo_palabras[palabra_limpia] += 1
        # Si la palabra no existe la añadimos e inicializamos su conteo en 1
        else:
            conteo_palabras[palabra_limpia] = 1

    return conteo_palabras

texto = "Este es un ejemplo. Ejemplo de texto. ¡Es un texto de ejemplo!"
resultado = contar_palabras(texto)

for palabra, recuento in resultado.items():
    print(f"{palabra}: {recuento}")
