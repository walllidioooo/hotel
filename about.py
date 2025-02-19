import flet as ft
from components import nav_bar

def about_page(page):
    return ft.View(
        route="/about",
        controls=[
            ft.Text("ℹ️ About Page", size=30),
            ft.ElevatedButton("Go to Home", on_click=lambda e: page.go("/")),
            ft.ElevatedButton("Go to Contact", on_click=lambda e: page.go("/contact")),
            nav_bar(page)
        ]
    )
