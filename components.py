import flet as ft

def nav_bar(page):
    """Navigation bar for all pages."""
    return ft.Row(
        [
            ft.ElevatedButton("🏠 Home", on_click=lambda e: page.go("/")),
            ft.ElevatedButton("ℹ️ About", on_click=lambda e: page.go("/about")),
            ft.ElevatedButton("📞 Contact", on_click=lambda e: page.go("/contact")),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
