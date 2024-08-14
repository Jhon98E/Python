"""
Ejercicio: 
    Implementa el algoritmo de ordenamiento por selección 
    para ordenar un arreglo de enteros en orden ascendente.

    Ejemplo:

        Considera la lista [64, 25, 12, 22, 11].

        --> En la primera pasada, encontramos que 11 es el elemento más pequeño, así que lo intercambiamos con 64. La lista queda [11, 25, 12, 22, 64].
        --> En la segunda pasada, encontramos que 12 es el siguiente elemento más pequeño, así que lo intercambiamos con 25. La lista queda [11, 12, 25, 22, 64].
        --> Y así sucesivamente, hasta que la lista esté completamente ordenada.
        
        Pistas para la implementación en codigo:

        --> Dos bucles: Necesitarás un bucle externo para iterar sobre cada elemento de la lista y un bucle interno para encontrar el mínimo en la parte no ordenada.
        -->Variable para el mínimo: Utiliza una variable para almacenar el índice del elemento más pequeño encontrado en cada iteración.
        --> Intercambio de elementos: Utiliza una variable temporal para intercambiar dos elementos.
"""


def ordenamiento_seleccion ( arreglo:list ) -> list:
    """
    Ordena una lista utilizando el algoritmo de ordenamiento por selección.

    Args:
        arreglo: La lista a ordenar.

    Returns:
        La lista ordenada en forma ascendente.
    """

    for i in range( len( arreglo ) - 1 ): # Bucle externo para iterar sobre cada elemento de la lista
        indice_minimo = i # Variable para definir el elemento mas pequeño en cada iteracción

        for j in range(( i + 1 ), len( arreglo )): # Bucle interno para buscar el elemento mas pequeño
            if arreglo[j] < arreglo[indice_minimo]: # Comparar si el elemento actual es menor que el minimo actual
                indice_minimo = j # Actualiza el valor minimo
        
        arreglo[i], arreglo[indice_minimo] = arreglo[indice_minimo], arreglo[i] # Intercambiar el elemento minimo por el elemento en la posicion i
    
    return arreglo
            

arreglo = [64, 25, 12, 22, 11]
resultado = ordenamiento_seleccion( arreglo )
print ( resultado )
