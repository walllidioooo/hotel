import flet as ft
from components import nav_bar

def contact_page(page):
    return ft.View(
        route="/contact",
        controls=[
            ft.Text("📞 Contact Page", size=30),
            ft.ElevatedButton("Go to Home", on_click=lambda e: page.go("/")),
            ft.ElevatedButton("Go to About", on_click=lambda e: page.go("/about")),
            nav_bar(page)
        ]
    )
