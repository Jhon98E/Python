"""
Ejercicio: 
    Implementa el algoritmo de ordenamiento de burbuja 
    para ordenar un arreglo de enteros en orden ascendente.

    Ejemplo:

        Considera la lista [3, 1, 4, 1, 5].

        Pasada 1:
        --> Comparamos 3 y 1, los intercambiamos: [1, 3, 4, 1, 5]
        --> Comparamos 3 y 4, no se intercambian.
        --> Comparamos 4 y 1, los intercambiamos: [1, 3, 1, 4, 5]
        ... (continúa hasta el final de la lista)

        Pasada 2:
        ... (se repite el proceso, pero posiblemente con menos intercambios)
        ...
        --> Pasadas sucesivas: Se siguen realizando pasadas hasta que no se produzcan más intercambios.

        Pistas para la implementación en codigo:

        --> Bucles anidados: Necesitarás dos bucles anidados para recorrer la lista y comparar elementos adyacentes.
        --> Condicional: Un condicional if te permitirá comparar elementos e intercambiarlos si es necesario.
        --> Función: Define una función para encapsular el algoritmo y hacerla reutilizable.
        --> Intercambio de elementos: Para intercambiar dos elementos en una lista, puedes usar una variable temporal.
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
