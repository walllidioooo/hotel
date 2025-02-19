import flet as ft
from home import home_page
from about import about_page
from contact import contact_page
from rooms import rooms_page


def main(page: ft.Page):
    page.title = "My Flet app"
    page.theme_mode = "light"

    def route_change(e):
        page.views.clear() 

        if page.route == "/":
            page.views.append(home_page(page))
        elif page.route == "/about":
            page.views.append(about_page(page))
        elif page.route == "/contact":
            page.views.append(contact_page(page))
        elif page.route == "/rooms":
            page.views.append(rooms_page(page))    

        
        page.update()

    page.on_route_change = route_change
    page.go("/")  # Start at the home page

if __name__=="__main__":
    ft.app(target=main)
