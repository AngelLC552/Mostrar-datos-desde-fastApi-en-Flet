import flet as ft
from app.styles.estilos import Colors, Buttons
import asyncio

async def show_popup(page: ft.Page, title: str, message: str, bgcolor:str=Colors.DANGER, txtcolor:str=Colors.WHITE):
    dlg = ft.AlertDialog(
        title_padding=0, 
        content_padding=0,
        title=ft.Container(
            bgcolor=bgcolor,
            padding=12,
            border_radius=ft.BorderRadius(18, 18, 0, 0),
            content=ft.Text(title,color=txtcolor,weight=ft.FontWeight.BOLD)
        ),
        content=ft.Container(
            padding=10,
            content=ft.Text(message),
        ),
        actions=[ft.Button("OK", on_click=lambda e: close_popup(page), style=Buttons.BUTTON_PRIMARY)]
    )
    page.show_dialog(dlg)


def close_popup(page: ft.Page):
    pop = getattr(page, "pop_dialog", None)
    if callable(pop):
        page.pop_dialog()
    page.update()


async def show_popup_auto_close(page: ft.Page, title: str, message: str, bgcolor:str=Colors.DANGER, txtcolor:str=Colors.WHITE, seconds: int = 3):
    dlg = ft.AlertDialog(
        title_padding=0, 
        content_padding=0,
        title=ft.Container(
            bgcolor=bgcolor,
            padding=12,
            border_radius=ft.BorderRadius(18, 18, 0, 0),
            content=ft.Text(title,color=txtcolor,weight=ft.FontWeight.BOLD)
        ),
        content=ft.Container(
            padding=10,
            content=ft.Text(message),
        )
    )    

    page.show_dialog(dlg)

    await asyncio.sleep(seconds)

    pop = getattr(page, "pop_dialog", None)
    if callable(pop):
        pop()

    page.update()


async def show_snackbar(page: ft.Page, title:str, message: str, bgcolor: str=Colors.DANGER, txtcolor:str=Colors.WHITE, seconds: int = 3) -> None:
    sb = ft.SnackBar(
        content=ft.Text(message, color=txtcolor),
        bgcolor=bgcolor,
        duration=ft.Duration(seconds=seconds),
    )
    page.show_dialog(sb)
