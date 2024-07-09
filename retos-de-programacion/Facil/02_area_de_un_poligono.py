"""
Crea una única función (importante que sólo sea una) que sea capaz de:
    --> Calcular y Retornar el área de un polígono.
        --> La función recibirá por parámetro sólo UN polígono a la vez.
        --> Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
        --> Imprime el cálculo del área de un polígono de cada tipo.
"""

def calcular_area(poligono):
    if poligono == "triangulo":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")

    elif poligono == "cuadrado":
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = lado ** 2
        print(f"El área del cuadrado es: {area}")

    elif poligono == "rectangulo":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = base * altura
        print(f"El área del rectángulo es: {area}")

    else:
        print("El polígono ingresado no es válido.")

poligono = input("Ingrese el nombre del poligono: ")
calcular_area(poligono.lower())