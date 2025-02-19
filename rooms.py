import flet as ft
from components import nav_bar
import utils
import database 

def rooms_page(page:ft.Page):

    def save_get():
        database.add_room(is_payed.value,is_aviable.value,people_inside.value)
        utils.get_rooms_file()
#update_room_status(room_id, is_available=None, is_paid=None, people_inside=None)

    def update_get(room_id, is_available, is_paid, people_inside):
        database.update_room_status(room_id, is_available, is_paid, people_inside)

        utils.get_rooms_file()
        pass


#room_id.value, is_aviable.value, is_payed.value, people_inside.value
    save_button=ft.ElevatedButton("save",on_click=lambda e:save_get())

    update_button=ft.ElevatedButton("update",on_click=lambda e:update_get(room_id.value, is_aviable.value, is_payed.value, people_inside.value))


    room_id=ft.TextField(
        label="room_id",        
          text_size=20,
            label_style=ft.TextStyle(size=18, color="gray")  #  not Only allow number input
        )
    people_inside = ft.TextField(
        label="people_inside",
        text_size=20 ,
        label_style=ft.TextStyle(size=18, color="gray") #  not Only allow number input
        )
    is_aviable=ft.Checkbox(label="tab if its aviable",
                           label_style=ft.TextStyle(size=20))
    is_payed=ft.Checkbox(label="tab if its payed",
                         label_style=ft.TextStyle(size=20))


    sub_cont_details=ft.Column(controls=[room_id,
                                         people_inside,
                                         is_payed,
                                         is_aviable,
                                         update_button,])
  
  #main funcction000000000000000000000000000

    def list_sub_containers():
        containers_main_list=ft.Row(controls=[],wrap=True,scroll="always")
        
        for i in database.get_rooms():
           
            for j in range(len(i)):
                
                sub_cont_details.controls[j]=ft.Text(f"{i[j]}thisss")
                #room_id, is_aviable, is_payed, people_inside
               
            
                 
            sub_container=ft.Container(
                    content=sub_cont_details,
                    padding=10,
                    bgcolor="orange",
                    height=270,
                    width=200,
                    border_radius=15,
                    border=ft.border.all(4,color="black"),    
                         )
            print("\n sub container content from the container",sub_container.content.controls[0],sub_container.content.controls[1],"ennnnnnd \n \n")
            containers_main_list.controls.append(sub_container)
        container_rooms=ft.Container(
        width=1200,
        height=680,
        content=containers_main_list,
        bgcolor="blue",
        padding=20,
        border=ft.border.all(4,"black"),
        border_radius=20,
    )    
        page.update()

        #print("the outer container room content(a row) controls[0] and [1] ",container_rooms.content.controls[0],"zzzzzzz",container_rooms.content.controls[1])
        return  container_rooms
          
    container_rooms= list_sub_containers()#ll be add in the end of the code   


    #containers list the      main_list
   
    
   
    
        #print(i,end="-______________________________-")#contro list >>>>>>< the room_id
    




   

    main_text=ft.Text("🏠 Home Page", size=30,)
    about_button=ft.ElevatedButton(" About", on_click=lambda e: page.go("/about"))
    contact_button=ft.ElevatedButton(" contact", on_click=lambda e: page.go("/contact"))


#saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaave

    def show_dialog(e):
        def close_dialog(e):
            dialog.open = False
            page.update()
        # Create a dialog with custom content
        print("has been performede0000000000000000000000000000000")
        dialog = ft.AlertDialog(
            title=ft.Text("Custom Window"),

            content=ft.Column(controls=[
                ft.Text("This is a custom window!"),
                sub_cont_details,
                save_button,
                ft.ElevatedButton("Close", on_click= close_dialog)
            ],),
            
        )
        # Show the dialog
        
        
        dialog.open = True
        page.overlay.append(dialog)
        page.update()


    add_room_button=ft.ElevatedButton("add room",on_click=show_dialog)


    return ft.View(
        route="/rooms",
        controls=[
            
            ft.Row(controls=[main_text,about_button,contact_button,add_room_button],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[container_rooms,],alignment=ft.MainAxisAlignment.CENTER),
            nav_bar(page),  # Navigation bar
        ],
        
        horizontal_alignment=ft.MainAxisAlignment.CENTER
    )

