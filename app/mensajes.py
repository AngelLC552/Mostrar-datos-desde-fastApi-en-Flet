import flet as ft

from app.styles.estilos import Buttons, Colors, Inputs, Textos_estilos
from app.components.popup import show_popup_auto_close


def mensajes_view(page: ft.Page):

    title = ft.Text(
        "Mi app Flet",
        style=Textos_estilos.H4,
        text_align=ft.TextAlign.CENTER
    )

    subtitle = ft.Text(
        "Sistema de estilos centralizado",
        style=Textos_estilos.H5
    )

    name = ft.TextField(
        label="Nombre",
        **Inputs.INPUT_PRIMARY
    )

    async def on_click(e):
        await show_popup_auto_close(
            page,
            "Saludo",
            f"Hola {name.value}",
            Colors.PRIMARY,
            Colors.WHITE,
            3
        )

    btn = ft.Button(
        "Saludar",
        on_click=on_click,
        style=Buttons.BUTTON_PRIMARY
    )

    return ft.Column(
        [title, subtitle, name, btn],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
