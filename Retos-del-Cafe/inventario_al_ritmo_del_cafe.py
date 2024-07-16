class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"""
        Producto: {self.nombre}
        Cantidad: {self.cantidad}
        Precio: ${self.precio:.2f}
        """

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, cantidad, precio):
        if nombre in self.productos:
            self.productos[nombre].cantidad += cantidad
        else:
            self.productos[nombre] = Producto(nombre, cantidad, precio)
        print(f"Producto '{nombre}' agregado o actualizado en el inventario.")

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            print(f"Producto '{nombre}' eliminado del inventario.")
        else:
            print(f"Producto '{nombre}' no encontrado en el inventario.")

    def actualizar_cantidad(self, nombre, nueva_cantidad):
        if nombre in self.productos:
            self.productos[nombre].cantidad = nueva_cantidad
            print(f"Cantidad del producto '{nombre}' actualizada a {nueva_cantidad}.")
        else:
            print(f"Producto '{nombre}' no encontrado en el inventario.")

    def generar_informe(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        print("Informe del inventario actual:")
        for producto in self.productos.values():
            print(producto)

def menu():
    inventario = Inventario()
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad")
        print("4. Generar informe")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto: ")
            nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            inventario.actualizar_cantidad(nombre, nueva_cantidad)
        elif opcion == "4":
            inventario.generar_informe()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    menu()
