import flet as flt
from calculadora_app import CalculadoraApp

def main(pagina: flt.Page):
    pagina.title = "Calculadora"
    pagina.window_maximizable = False
    pagina.window_minimizable = False
    pagina.window_width = 390
    pagina.window_height = 350
    calculadora = CalculadoraApp()

    pagina.add(calculadora)

flt.app(target=main)