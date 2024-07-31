"""
Crea un programa que se encargue de transformar un número decimal a binario
sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

def decimal_a_binario(numero:int):
    """Convierte un número decimal a binario.

    Args:
        numero: El número decimal a convertir.

    Returns:
        Una cadena con la representación binaria del número.
    """
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero //= 2
    return binario

numero_decimal = 42
resultado = decimal_a_binario(numero_decimal)
print(f"El numero decimal {numero_decimal} en binario es: {resultado}")