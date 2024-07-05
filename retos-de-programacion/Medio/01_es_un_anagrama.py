"""
Escribe una función que reciba dos palabras (String) y retorne:
verdadero o falso (Bool) según sean o no anagramas.
    --> Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
    --> NO hace falta comprobar que ambas palabras existan.
    --> Dos palabras exactamente iguales no son anagrama.
"""


def es_un_anagrama ( palabra1, palabra2 ):

    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    if palabra1 == palabra2 :
        return False
    
    if len(palabra1) != len(palabra2):
        return False
    
    return sorted(palabra1) == sorted(palabra2)


print(es_un_anagrama("Roma", "amor"))
print(es_un_anagrama("Roma", "roma"))
print(es_un_anagrama("Roma", "Ramo"))
print(es_un_anagrama("Roma", "Romero"))