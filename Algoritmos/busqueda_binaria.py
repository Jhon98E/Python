"""
Ejercicio: 
    Dado un arreglo de enteros ordenados, 
    implementa una búsqueda binaria para encontrar un número 
    y devolver su índice. 
    Si el número no está presente, devuelve -1.
"""


def busqueda_binaria (arreglo: list[int], numero: int) -> int:
    """
    Realiza una búsqueda binaria en un arreglo ordenado.

    Args:
        arreglo: Un arreglo ordenado de números enteros.
        numero: El número a buscar.

    Returns:
        El índice del número en el arreglo si se encuentra, -1 en caso contrario.
    """

    izquierda = 0
    derecha = len(arreglo) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if arreglo[medio] == numero:
            return medio
        elif numero < arreglo[medio]:
            derecha = medio -1
        else:
            izquierda = medio + 1

    return -1


arreglo = [2, 4, 6, 8, 10, 12]
numero = 8
resultado = busqueda_binaria(arreglo, numero)
print(resultado)