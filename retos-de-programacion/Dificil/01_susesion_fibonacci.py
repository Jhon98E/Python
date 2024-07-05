"""
Escribe un programa que imprima los 50 primeros números de la sucesión.
de Fibonacci empezando en 0.
    --> La serie fibonacci es una sucesión de numeros en la que:
        -> El siguiente numero es la suma de los dos anteriores.
        ejemplo: 0,1,1,2,3,5,8,13,...
"""

fibonacci = [0,1]

while len(fibonacci) < 50:
    siguiente_numero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente_numero)
    
for indice, numero in enumerate(fibonacci):
    print(f"{indice} --> {numero}")
