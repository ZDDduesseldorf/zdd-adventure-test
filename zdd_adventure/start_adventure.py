"""This starts the adventure
"""
import zdd_adventure.save as save
import zdd_adventure.room_basement_1 as room_basement_1

end_game = False

def start():
    for _ in range(5):
        print(20 * ">")
    print(">>>> Something awesome is about to happen...")
    for _ in range(5):
        print(20 * ">")
    print(">>>> Loading Data...")
    #spieldaten laden
    data = save.load_data()
    print(data)
    floor = {1: room_basement_1.room_basement_1(data)}
    while not end_game:
        floor[data["floor"]]
    
    

start()