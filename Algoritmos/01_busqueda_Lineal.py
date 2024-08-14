"""
Ejercicio:
    Implementa un algoritmo de búsqueda lineal
    que busque un número en un arreglo de enteros
    y devuelva su índice.
    Si el número no está presente,
    devuelve -1.

    Ejemplo en lenguaje natural:
        Imagina que tienes una caja de juguetes y quieres encontrar tu carrito rojo. 
        Empiezas a revisar cada juguete uno por uno, empezando por el primero. 
        Si encuentras el carrito rojo, dices "¡Aquí está!" y te detienes. 
        Si revisas todos los juguetes y no encuentras el carrito rojo, dices "No está aquí".

        Pistas para la implementación en codigo:

        --> Estructura de datos: Usa una lista para representar el arreglo.
        --> Bucle: Un bucle for es ideal para recorrer todos los elementos de la lista.
        --> Condicional: Un if te permitirá comparar elementos y tomar decisiones.
        --> Función: Define una función para encapsular el algoritmo y hacerla reutilizable.
"""


def busqueda_lineal(arreglo: list[int], numero: int):
    """
    Realiza una búsqueda lineal para encontrar un número en un arreglo.

    Recorre el arreglo elemento por elemento y compara cada uno con el número
    buscado. Si encuentra una coincidencia, devuelve el índice. De lo contrario,
    devuelve -1.

    Args:
        arreglo: Una lista de números enteros donde realizar la búsqueda.
        numero: El número a buscar.

    Returns:
        El índice del número en el arreglo si se encuentra, -1 en caso contrario.

    Raises:
        TypeError: Si el argumento `arreglo` no es una lista.
    """

    if not isinstance(arreglo, list):
        raise TypeError("El argumento 'arreglo' debe ser una lista")

    for i, elemento in enumerate(arreglo):
        if elemento == numero:
            return i
        
    return -1

# arreglo = "Hola Mundo"
arreglo = [10, 20, 30, 40, 50]
numero = 30
resultado = busqueda_lineal(arreglo, numero)

if resultado != ( -1 ):
    print(f"La posicion del numero {numero} es: {resultado}")
else:
    print(resultado)
