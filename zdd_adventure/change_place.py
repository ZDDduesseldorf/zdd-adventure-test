import os
import zdd_adventure.room_basement_1 as room_basement_1




def chose_between_2():
    chose = ""
    while chose != "1" and chose != "2": 
        chose = input("Chose:")
    return chose

def room_action(data, command):
    floor_rooms = {
        -1: {"name": "Basement",
             0: {"func": "",
                 "name": "Corridor"},
             1: {"func": room_basement_1.room_basement_1(data),
                 "name": "Room 1"}
        }
    }
    print(data, command)
    
    if command == "floor":
        floors = list(floor_rooms.keys())
        for floor in floors:
            print(floor, floor_rooms[floor]["name"])
    elif command == "room":
        rooms = list(floor_rooms[data["floor"]].keys())
        for room in rooms:
            print(room, floor_rooms[room]["name"])
    return floor_rooms[data["floor"]][data["room"]][command]

def change_place(data):
    os.system('cls')
    if data["room"] == 0:
        print(f"Where does {data['name']} want to go now?\n\n1 another floor\n2 another room\n\n")
        chose = chose_between_2()
        if chose == "1":
            print("Which floor does {data['name']} want to go?\n\n")
            room_action(data, "floor")
            
        else:
            print(f"Which room does {data['name']} want to enter?\n\n")
            room_action(data, "room")
    else:
        print(f"Where does {data['name']} want to go now?\n\n1 Back to the corridor\n2 stay here\n\n")
        chose = chose_between_2()
        if chose == "1":
            data["room"] = 0
    return data