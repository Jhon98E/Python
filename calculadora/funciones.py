class FuncionesOnClick:
    def __init__(self, calculadora):
        self.calculadora = calculadora
        self.reset()

    def formato_numero(self, numero):
        if numero % 1 == 0:
            return int(numero)
        else:
            return numero

    def calcular(self, operacion1, operacion2, operador):
        if operador == "+":
            return self.formato_numero(operacion1 + operacion2)
        elif operador == "-":
            return self.formato_numero(operacion1 - operacion2)
        elif operador == "*":
            return self.formato_numero(operacion1 * operacion2)
        elif operador == "/":
            if operacion2 == 0:
                return "Error"
            else:
                return self.formato_numero(operacion1 / operacion2)

    def reset(self):
        self.operador = "+"
        self.operacion1 = 0
        self.nueva_operacion = True

    def click_boton(self, evento):
        datos = evento.control.text
        print(f"Botón pulsado con datos = {datos}")

        if self.calculadora.resultado.value == "Error" or datos == "AC":
            self.calculadora.resultado.value = "0"
            self.reset()

        elif datos in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]:
            if self.calculadora.resultado.value == "0" or self.nueva_operacion:
                self.calculadora.resultado.value = datos
                self.nueva_operacion = False
            else:
                self.calculadora.resultado.value += datos

        elif datos in ["/", "*", "-", "+"]:
            self.calculadora.resultado.value = str(self.calcular(
                self.operacion1,
                float(self.calculadora.resultado.value),
                self.operador
            ))
            self.operador = datos
            if self.calculadora.resultado.value == "Error":
                self.operacion1 = 0
            else:
                self.operacion1 = float(self.calculadora.resultado.value)

            self.nueva_operacion = True

        elif datos == "=":
            self.calculadora.resultado.value = str(self.calcular(
                self.operacion1,
                float(self.calculadora.resultado.value),
                self.operador
            ))
            self.reset()

        elif datos == "%":
            self.calculadora.resultado.value = str(float(self.calculadora.resultado.value) / 100)
            self.reset()

        elif datos == "+/-":
            if float(self.calculadora.resultado.value) > 0:
                self.calculadora.resultado.value = "-" + self.calculadora.resultado.value
            elif float(self.calculadora.resultado.value) < 0:
                self.calculadora.resultado.value = str(
                    self.formato_numero(abs(float(self.calculadora.resultado.value)))
                )

        self.calculadora.update()
