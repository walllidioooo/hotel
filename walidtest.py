







x=5
def f(x=0):
    print(x)
f(x)    


















"""import flet as ft

def main(page: ft.Page):
    draggable_window = ft.Draggable(
        content=ft.Container(
            width=250,
            height=150,
            bgcolor="white",
            border_radius=10,
            shadow=ft.BoxShadow(blur_radius=10, spread_radius=3, color="gray"),
            padding=20,
            content=ft.Column([
                ft.Text("Draggable Window"),
                ft.ElevatedButton("Close", on_click=lambda e: setattr(draggable_window, "visible", False) or page.update()),
            ]),
        )
    )

    page.add(
        ft.Stack([
            ft.Column([ft.Text("Main Interface"), draggable_window])
        ])
    )

ft.app(target=main)"""










"""   def list_sub_containers(target,rooms_number):
        main_list=ft.Row(controls=[],wrap=True,scroll="always")
        
        for i in database.get_rooms():
           
            for j in range(len(i)):
                
                sub_cont_details.controls[j]=ft.Text(f"{i[j]}thisss")
                #room_id.value, is_aviable.value, is_payed.value, people_inside.value
                
            print("thoiiiiiis is the sub list",sub_cont_details.controls)    
                 
            sub_container=ft.Container(
                    content=sub_cont_details,
                    padding=10,
                    bgcolor="orange",
                    height=270,
                    width=200,
                    border_radius=15,
                    border=ft.border.all(4,color="black"),    
                         )

            
            main_list.controls.append(sub_container)
            print(main_list)
            page.update()
        return main_list   
            






    rooms_number= int(utils.get_rooms_file())
    print("the main list l perform here  list_sub_containers")
    mainlist=list_sub_containers(sub_container,rooms_number)
    for i in mainlist:
        pass
    """

















list=[5,8,5,8,5]
arr=[]
for j in range (5):

    for i in range (len(list)):
        list.append(i+1)
    arr.append(list)
    print (arr)

