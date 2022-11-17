import os
import zdd_adventure.room_basement_1 as room_basement_1
import zdd_adventure.closed_room_first_floor as crff

floor_rooms = {
        -1: {"name": "Basement",
             0: {"func": "",
                 "name": "Corridor"},
             1: {"func": room_basement_1.room_basement_1,
                 "name": "Room 1"}
        },
        1: {"name": "First Floor",
             0: {"func": "",
                 "name": "Corridor"},
             3: {"func": crff.closed_room_first_floor,
                 "name": "Closed Room"}
        }
    }


def chose_between_2():
    chose = ""
    while chose != "1" and chose != "2": 
        chose = input("Chose:")
    return chose

def chose_between_list(l):
    chose = ""
    while not chose in l: 
        chose = input("Please decide:")
    return chose
     

def change_place(data):
    os.system('cls')
    if data["room"] == 0:
        print(f"Where does {data['name']} want to go now?\n\n1 another floor\n2 another room\n\n")
        chose = chose_between_2()
        if chose == "1":
            print(f"Which floor does {data['name']} want to go?\n\n")
            floors = list(floor_rooms.keys())
            floor_list = []
            for floor in floors:
                print(floor, floor_rooms[floor]["name"])
                floor_list.append(str(floor))
            data["floor"] = chose_between_list(floor_list)
            
        else:
            print(f"Which room does {data['name']} want to enter?\n\n")
            rooms = list(floor_rooms[data["floor"]].keys())
            room_list = []
            for room in rooms:
                if room != "name":
                    print(room, floor_rooms[data["floor"]][room]["name"])
                    room_list.append(str(room))
            data["room"] = chose_between_list(room_list)
    else:
        print(f"Where does {data['name']} want to go now?\n\n1 Back to the corridor\n2 stay here\n\n")
        chose = chose_between_2()
        if chose == "1":
            data["room"] = 0
    return data