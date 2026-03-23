import flet as ft
from typing import Any

from app.styles.estilos import Colors, Textos_estilos, Card  # si no tienes estilos puedes quitar esto


def products_view(page: ft.Page) -> ft.Control:

    rows_data: list[dict[str, Any]] = []
    total_items = 0

    total_text = ft.Text(
        "Total de productos: (cargando...)",
        style=Textos_estilos.H4
    )

    # Encabezados
    columnas = [
        ft.DataColumn(label=ft.Text("Nombre", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Cantidad", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Ingreso", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Min", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Max", style=Textos_estilos.H4)),
    ]

    # Datos de prueba
    data = []
    data.append(
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text("nombre1...")),
                ft.DataCell(ft.Text("cantidad1...")),
                ft.DataCell(ft.Text("ingreso1...")),
                ft.DataCell(ft.Text("min1...")),
                ft.DataCell(ft.Text("max1...")),
            ]
        )
    )

    # Tabla
    tabla = ft.DataTable(
        columns=columnas,
        rows=data,
        width=900,
        heading_row_height=60,
        heading_row_color=Colors.BG,
        data_row_max_height=60,
        data_row_min_height=48,
    )

    return ft.Column(
        [
            total_text,
            tabla
        ]
    )