import flet as ft
import database
   

#write in file and return number of records
def get_rooms_file():
        text=""
        i=0
        with open("hotel_costum","w") as file:
            for i,room in enumerate(database.get_rooms()):
                text+=str(room)+"\n"
                print("rooms index",i)
            file.write(text)
            if i !=0:
                return i
            return 0


        
        

