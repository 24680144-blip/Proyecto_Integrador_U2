import flet as ft
from data_manager import productos
from custom_card import ProductoCard

def main(page: ft.Page):
    page.title = "TechStore - Catálogo de Productos"
    page.padding = 0  
    page.bgcolor = ft.Colors.GREY_50
    page.scroll = ft.ScrollMode.AUTO

    header = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("TECHSTORE", size=35, weight="bold", color=ft.Colors.BLUE_900),
                ft.Text("Desarrollo de Componentes Reutilizables - Unidad 2", size=15, color=ft.Colors.BLUE_GREY_400),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
        padding=ft.Padding.symmetric(vertical=30, horizontal=50),
        bgcolor=ft.Colors.WHITE,
        width=float("inf"), 
        border=ft.Border.only(bottom=ft.BorderSide(2, ft.Colors.BLUE_100)),
        shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.BLACK_12),
    )

    catalogo_grid = ft.Row(
        wrap=True, 
        spacing=25,
        run_spacing=25,
        alignment=ft.MainAxisAlignment.CENTER, 
        controls=[ProductoCard(p) for p in productos] 
    )

    body = ft.Container(
        content=catalogo_grid,
        padding=ft.Padding.symmetric(vertical=40, horizontal=20),
        alignment=ft.Alignment(0, -1) 
    )

    page.add(header, body)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")