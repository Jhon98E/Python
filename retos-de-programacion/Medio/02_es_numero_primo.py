"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
    --> Para determinar que un numero es primo se debe tener en cuenta:
        --> Un número primo es aquel que solo es divisible por 1 y por el mismo número.
        --> Un numero primo no debe ser menor a 2
        --> El numero 2 y 3 son los primeros numeros primos de la secuencia.
        --> Un numero primo no debe ser divisible entre 2 y 3.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def es_primo(numero):
    if numero < 2:
        return False
    
    if numero == 2 or numero == 3:
        return True
    
    if numero % 2 == 0 and numero != 2:
        return False
    
    if numero % 3 == 0 and numero != 3:
        return False
    
    iterador = 5

    while ( iterador ** 2 ) <= numero:
        if ( numero % iterador == 0 ) and ( numero % ( iterador + 2 ) == 0 ):
            return False
        
        iterador += 6

    return True

for numero in range( 1, 101, 1):
    if es_primo(numero):
        print(numero)

# for numero in range( 1, 101, 1):
#     if es_primo(numero):
#         print(f"El numero {numero} es primo")
#     else:
#         print(f"El numero {numero} no es primo")