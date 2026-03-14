import flet as ft

class ProductoCard(ft.Container):
    def __init__(self, producto):
        super().__init__()
        self.width = 250
        self.bgcolor = ft.Colors.WHITE
        self.border_radius = 15
        self.padding = 15
        self.border = ft.Border.all(1, ft.Colors.OUTLINE_VARIANT)
        self.shadow = ft.BoxShadow(blur_radius=10, color=ft.Colors.BLACK_12)

        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Image(src=producto['imagen'], width=150, height=150, fit="contain"),
                ft.Text(producto['nombre'], weight="bold", size=16),
                ft.Text(producto['descripcion'], size=12, color="grey"),
                ft.Text(f"${producto['precio']}", color="green", size=18, weight="bold"),
                ft.Row(
                    [
                        ft.IconButton(ft.Icons.FAVORITE_BORDER),
                        ft.FilledButton("Agregar", icon=ft.Icons.ADD_SHOPPING_CART)
                    ],
                    alignment="center"
                )
            ]
        )