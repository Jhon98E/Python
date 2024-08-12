"""
Ejercicio: 
    Implementa el algoritmo de ordenamiento de burbuja 
    para ordenar un arreglo de enteros en orden ascendente.
"""


def ordenamiento_burbuja (arreglo:list) -> list:
    """
    Ordena una lista utilizando el algoritmo de burbuja.

    Args:
        arreglo: La lista a ordenar.

    Returns:
        La lista ordenada en forma ascendente.
    """

    for i in range(len(arreglo)): # Bucle externo: controla el número de pasadas
        for j in range(len(arreglo) - i - 1): # Bucle interno: compara elementos adyacentes e intercambia si es necesario

            if arreglo[j] > arreglo[j + 1]: # Si el elemento actual es mayor al siguiente
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j] # Intercambiar elementos

    return arreglo

arreglo = [3, 1, 4, 1, 5]
resultado = ordenamiento_burbuja(arreglo)
print (resultado)
