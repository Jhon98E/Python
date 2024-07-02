import flet as flt
from funciones import FuncionesOnClick

class CalculadoraApp(flt.Container):
    def __init__(self):
        super().__init__()
        
        self.resultado = flt.Text(value=0, color="white", size=20)

        botones = [
            "AC", "+/-", "%", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "=",
        ]

        self.funciones = FuncionesOnClick(self)

        filas_botones = []
        fila = []

        for i, boton in enumerate(botones):
            btn = flt.ElevatedButton(
                text=boton,
                on_click=self.funciones.click_boton
            )

            if boton in ["AC", "+/-", "%"]: 
                btn.expand=1
                btn.bgcolor=flt.colors.BLUE_GREY_100
                btn.color=flt.colors.BLACK

            elif boton in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]:
                btn.expand=1
                btn.bgcolor=flt.colors.WHITE24
                btn.color=flt.colors.BLACK

            elif boton in ["/", "*", "-", "+"]:
                btn.expand=1
                btn.bgcolor=flt.colors.ORANGE
                btn.color=flt.colors.BLACK

            elif boton in ["="]:
                btn.expand=2
                btn.bgcolor=flt.colors.ORANGE
                btn.color=flt.colors.BLACK
            
            fila.append(btn)

            if ( i + 1 ) % 4 == 0:
                filas_botones.append(flt.Row(controls=fila))
                fila = []


        if fila :
            filas_botones.append(flt.Row(controls=fila))

        self.content = flt.Column(
                controls=[
                    flt.Row(controls=[self.resultado], alignment="end"),
                    *filas_botones,
                ],
                spacing=10,
                alignment="center"
            )        
        self.bgcolor = "black"
        self.border_radius = 20
        self.padding = 20
        self.width = 350
