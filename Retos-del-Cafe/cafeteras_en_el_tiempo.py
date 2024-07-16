from Crypto.Cipher import AES
import base64


class EventoHistorico:
    def __init__(self, id_evento, fecha, descripcion, consecuencias=[]):
        self.id_evento = id_evento
        self.fecha = fecha
        self.descripcion = descripcion
        self.consecuencias = consecuencias
        self.modificaciones = []

    def modificar(self, nueva_fecha=None, nueva_descripcion=None):
        if nueva_fecha:
            self.modificaciones.append(f"Cambio de fecha de {self.fecha} a {nueva_fecha}")
            self.fecha = nueva_fecha
        if nueva_descripcion:
            self.modificaciones.append(f"Cambio de descripción de '{self.descripcion}' a '{nueva_descripcion}'")
            self.descripcion = nueva_descripcion


class GestorEventos:
    def __init__(self):
        self.eventos = []
        self.cifrado = SistemaCifrado()

    def agregar_evento(self, fecha, descripcion, consecuencias=[]):
        id_evento = len(self.eventos) + 1
        fecha_cifrada = self.cifrado.cifrar(fecha)
        descripcion_cifrada = self.cifrado.cifrar(descripcion)
        evento = EventoHistorico(id_evento, fecha_cifrada, descripcion_cifrada, consecuencias)
        self.eventos.append(evento)
        return evento

    def consultar_evento(self, id_evento):
        for evento in self.eventos:
            if evento.id_evento == id_evento:
                evento.fecha = self.cifrado.descifrar(evento.fecha)
                evento.descripcion = self.cifrado.descifrar(evento.descripcion)
                return evento
        return None

    def modificar_evento(self, id_evento, nueva_fecha=None, nueva_descripcion=None):
        evento = self.consultar_evento(id_evento)
        if evento:
            nueva_fecha_cifrada = self.cifrado.cifrar(nueva_fecha) if nueva_fecha else None
            nueva_descripcion_cifrada = self.cifrado.cifrar(nueva_descripcion) if nueva_descripcion else None
            evento.modificar(nueva_fecha_cifrada, nueva_descripcion_cifrada)
            self.actualizar_consecuencias(evento)
        return evento

    def eliminar_evento(self, id_evento):
        self.eventos = [evento for evento in self.eventos if evento.id_evento != id_evento]

    def actualizar_consecuencias(self, evento):
        for consecuencia_id in evento.consecuencias:
            consecuencia = self.consultar_evento(consecuencia_id)
            if consecuencia:
                # Aquí se debe implementar la lógica para actualizar la consecuencia basada en la modificación del evento original.
                pass


class MaquinaDelTiempo:
    def __init__(self, gestor_eventos):
        self.gestor_eventos = gestor_eventos

    def viajar_a_fecha(self, fecha):
        eventos_en_fecha = [evento for evento in self.gestor_eventos.eventos if self.gestor_eventos.cifrado.descifrar(evento.fecha) == fecha]
        return eventos_en_fecha


class SistemaCifrado:
    def __init__(self, key=b'Sixteen byte key'):
        self.key = key

    def cifrar(self, data):
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
        return base64.b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')

    def descifrar(self, enc_data):
        data = base64.b64decode(enc_data)
        nonce = data[:16]
        tag = data[16:32]
        ciphertext = data[32:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
        return cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8')


class InterfazUsuario:
    def __init__(self):
        self.gestor_eventos = GestorEventos()
        self.maquina_del_tiempo = MaquinaDelTiempo(self.gestor_eventos)

    def mostrar_menu(self):
        print("Sistema de Gestión de Eventos Históricos")
        print("1. Agregar Evento")
        print("2. Consultar Evento")
        print("3. Modificar Evento")
        print("4. Eliminar Evento")
        print("5. Viajar en el Tiempo")
        print("6. Salir")

    def iniciar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                fecha = input("Ingrese la fecha del evento (YYYY-MM-DD): ")
                descripcion = input("Ingrese la descripción del evento: ")
                self.gestor_eventos.agregar_evento(fecha, descripcion)
            elif opcion == "2":
                id_evento = int(input("Ingrese el ID del evento a consultar: "))
                evento = self.gestor_eventos.consultar_evento(id_evento)
                print(vars(evento) if evento else "Evento no encontrado")
            elif opcion == "3":
                id_evento = int(input("Ingrese el ID del evento a modificar: "))
                nueva_fecha = input("Ingrese la nueva fecha del evento (YYYY-MM-DD): ")
                nueva_descripcion = input("Ingrese la nueva descripción del evento: ")
                evento = self.gestor_eventos.modificar_evento(id_evento, nueva_fecha, nueva_descripcion)
                print(vars(evento) if evento else "Evento no encontrado")
            elif opcion == "4":
                id_evento = int(input("Ingrese el ID del evento a eliminar: "))
                self.gestor_eventos.eliminar_evento(id_evento)
            elif opcion == "5":
                fecha = input("Ingrese la fecha a la que desea viajar (YYYY-MM-DD): ")
                eventos_en_fecha = self.maquina_del_tiempo.viajar_a_fecha(fecha)
                for evento in eventos_en_fecha:
                    print(vars(evento))
            elif opcion == "6":
                break
            else:
                print("Opción no válida")


if __name__ == "__main__":
    interfaz = InterfazUsuario()
    interfaz.iniciar()
