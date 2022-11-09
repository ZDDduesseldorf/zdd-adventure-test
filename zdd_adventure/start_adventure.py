"""This starts the adventure
"""
import zdd_adventure.save as save

game_over = False

def start():
    for _ in range(5):
        print(20 * ">")
    print(">>>> Something awesome is about to happen...")
    for _ in range(5):
        print(20 * ">")
    print(">>>> Loading Data...")
    #spieldaten laden
    data = save.load_data()
    
    

start()