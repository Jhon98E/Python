"""
Ejercicio: 
    Dado un arreglo de enteros ordenados, 
    implementa una búsqueda binaria para encontrar un número 
    y devolver su índice. 
    Si el número no está presente, devuelve -1.

    Ejemplo:

        Supongamos que tienes un arreglo ordenado [2, 4, 6, 8, 10] y quieres buscar el número 6.

        --> Inicialmente, izquierda es 0 y derecha es 4.
        --> El punto medio es 2.
        --> El elemento en el índice 2 es 6, así que lo encontraste y devuelves 2.

        Pistas para la implementación en codigo:

        --> Estructura de datos: Usa una lista para representar el arreglo ordenado.
        --> Bucle: Un bucle while es ideal para repetir el proceso hasta encontrar el número o agotar las opciones.
        --> Condicionales: Usa if y elif para comparar elementos y tomar decisiones.
        --> Función: Define una función para encapsular el algoritmo y hacerla reutilizable.
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

if resultado != ( -1 ):
    print(f"La posicion del numero {numero} es: {resultado}")
else:
    print(resultado)