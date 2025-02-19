import flet as ft
from components import nav_bar

def home_page(page:ft.Page):

    button1=ft.ElevatedButton(text="start",width=250,height=70,)
    button2=ft.ElevatedButton(text="guguggu",width=250,height=70,)
    button3=ft.ElevatedButton(text="rooms",width=250,height=70,on_click=lambda e: page.go("/rooms"))
    button4=ft.ElevatedButton(text="exite",width=250,height=70,)
    sub_lists=ft.Column(controls=[
        button1,
        button2,
        button3,
        button4,
    ],
      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    
    scroll="always",

    )

    container=ft.Container(
        width=300,
        height=400,
        bgcolor="red",
        content=sub_lists,       
        border_radius=15,
        padding=30
    )
    return ft.View(
        route="/",
        controls=[
            
            ft.Row(controls=[ft.Text("🏠 Home Page", size=30,)],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[ft.ElevatedButton("Go to About", on_click=lambda e: page.go("/about"))],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[ft.ElevatedButton("Go to Contact", on_click=lambda e: page.go("/contact"))],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[container,],alignment=ft.MainAxisAlignment.CENTER),#mainnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
            nav_bar(page),  # Navigation bar
        ],
        horizontal_alignment=ft.MainAxisAlignment.CENTER
    )
