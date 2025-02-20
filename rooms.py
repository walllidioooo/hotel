import flet as ft
from components import nav_bar
import utils
import database 

def rooms_page(page:ft.Page):

    def save_get():
        database.add_room(is_payed.value,is_aviable.value,people_inside.value)
        list_sub_containers()
        utils.get_rooms_file()
        
        
#update_room_status(room_id, is_available=None, is_paid=None, people_inside=None)

    def update_get(room_id, is_aviable, is_payed, people_inside):
        database.update_room_status(room_id,is_payed,is_aviable,people_inside)
        utils.get_rooms_file()

        
    def update_get_dialog():
        show_dialog(button=update_button,idf=room_id)
        database.update_room_status(room_id.value,is_aviable.value,is_payed.value,people_inside.value)
        utils.get_rooms_file()

        pass    


#room_id.value, is_aviable.value, is_payed.value, people_inside.value
    save_button=ft.ElevatedButton("save",on_click=lambda e:save_get())

    update_button=ft.ElevatedButton("update",on_click=lambda e:update_get_dialog())

    
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
    

  
  #main funcction000000000000000000000000000

    def list_sub_containers():
        containers_main_list=ft.Row(controls=[],wrap=True,scroll="always")
        name_attr_list=["room_id","is avaible","is payed","people_inside"]
        for i in database.get_rooms():
            

            attr_list=[i[0],
                        "yess" if i[1]==1 else "noo"
                       ,"yess" if i[2]==1 else "noo",
                       i[3]]

           
            attr_list = ft.Column(controls=[ft.Text(f"{name_attr_list[index]}: {attr_list[index]}") for index in range (len(attr_list))               
            ])
            attr_list.controls.append(update_button)

            sub_container=ft.Container(

                  content=attr_list,
                    


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

    def show_dialog(button,idf):
        def close_dialog(e):
            dialog.open = False
            page.update()
        # Create a dialog with custom content
        print("has been performede0000000000000000000000000000000")
        dialog = ft.AlertDialog(
            title=ft.Text("Custom Window"),

            content=ft.Column(controls=[
                ft.Text("This is a custom window!"),
                idf,
                is_payed,
                is_aviable,
                people_inside,
                
                button,
                ft.ElevatedButton("Close", on_click= close_dialog)
            ],),
            
        )
        # Show the dialog
        
        
        dialog.open = True
        page.overlay.append(dialog)
        page.update()


    add_room_button=ft.ElevatedButton("add room",on_click=lambda e: show_dialog(save_button,ft.Text("........")))

    def refresh():
        page.go("/about")
        page.go("/rooms")



    refresh_button= ft.IconButton(
        icon=ft.icons.REFRESH,  # Choose an icon
        icon_size=30,  # Adjust size
        on_click=lambda e: refresh(),  # Define action on click
        tooltip="refresh",  # Tooltip on hover
    )
    return ft.View(
        route="/rooms",
        controls=[
            
            ft.Row(controls=[main_text,about_button,contact_button,add_room_button,refresh_button],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[container_rooms,],alignment=ft.MainAxisAlignment.CENTER),
            nav_bar(page),  # Navigation bar
        ],
        
        horizontal_alignment=ft.MainAxisAlignment.CENTER
    )

