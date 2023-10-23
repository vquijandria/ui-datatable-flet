import flet as ft
from flet import *
from header import AppHeader
from form import AppForm
from data_table import AppDataTable

def main(page: Page):
    page.bgcolor = "#FDFDFD"
    page.padding = 20
    page.add(
        # Columna principal donde ira y mostrara cada componente
        Column(
            expand = True,
            controls = [
                # Las instancias de la clase van aqui...
                AppHeader(),
                Divider(height=2, color="transperent"),
                AppForm(),
                Column(
                    scroll="hidden",
                    expand=True,
                    controls=[AppDataTable()]
                ),
            ],
        )
    )
    page.update()
    pass



if __name__ == '__main__':
    ft.app(target=main)