def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for i in range(len(texto)):
        char = texto[i]
        if char.isupper():
            resultado += chr((ord(char) + desplazamiento - 65) % 26 + 65)
        elif char.islower():
            resultado += chr((ord(char) + desplazamiento - 97) % 26 + 97)
        else:
            resultado += char
    return resultado

def descifrar_cesar(texto, desplazamiento):
    return cifrar_cesar(texto, -desplazamiento)


def mostrar_menu():
    print("1. Ingresar nuevo pedido")
    print("2. Mostrar pedidos cifrados")
    print("3. Mostrar pedidos descifrados")
    print("4. Salir")

def ingresar_pedido(pedidos, desplazamiento):
    pedido = input("Ingrese el pedido: ")
    pedido_cifrado = cifrar_cesar(pedido, desplazamiento)
    pedidos.append(pedido_cifrado)
    print("Pedido ingresado y cifrado correctamente.\n")

def mostrar_pedidos_cifrados(pedidos):
    print("Pedidos cifrados:")
    for pedido in pedidos:
        print(pedido)
    print()

def mostrar_pedidos_descifrados(pedidos, desplazamiento):
    print("Pedidos descifrados:")
    for pedido in pedidos:
        print(descifrar_cesar(pedido, desplazamiento))
    print()
    

def main():
    desplazamiento = 3
    pedidos = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ingresar_pedido(pedidos, desplazamiento)
        elif opcion == "2":
            mostrar_pedidos_cifrados(pedidos)
        elif opcion == "3":
            mostrar_pedidos_descifrados(pedidos, desplazamiento)
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.\n")

if __name__ == "__main__":
    main()
