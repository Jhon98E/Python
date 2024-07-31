"""
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
    --> Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""


def invertir_cadena(cadena:str):
    cadena_invertida:str = ""
    for elemento in range(len(cadena) - 1, -1, -1):
        cadena_invertida += cadena[elemento]
    return cadena_invertida

cadena = "Hola Mundo"
print(invertir_cadena(cadena))
