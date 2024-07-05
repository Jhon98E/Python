"""
Escribe un Programa que muestre por consola:
Los numeros del 1 al 100 sustituyendo los siguientes numeros.
    --> Los numeros que sean multiplos de 3 deben ser reemplazados por la palabra Fizz.
    --> Los numeros que sean multiplos de 5 deben ser reemplazados por la palabra Buzz.
    --> Los numeros que sean multiplos de 3 y de 5 deben ser reemplazados por la palabra FizzBuzz.
"""

for numero in range(1, (100 + 1)):
    if numero % 3 == 0 and numero % 5 == 0:
        print ("FizzBuzz")
    elif numero % 3 == 0:
        print ("Fizz")
    elif numero % 5 == 0:
        print ("Buzz")
    else:
        print (numero)