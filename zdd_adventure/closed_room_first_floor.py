# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:33:26 2022

@author: lizak
"""
from zdd_adventure.graphics import countdown, slow_print, ascii_output
from zdd_adventure.InputChecker_and_DrunkMode import player_input
import time
# the locked room on the 1st basement 

# the functionalities :
# input_check()
# closed_room_first_floor():
# switch_light_on():
# search_the_key()
# leave_room()

    
    
def closed_room_first_floor(game):
    text_1 = f"""
    WoOoooOw the kiddo did it...
    {game.name} is now in a new room, but can't see anything...
    it's dark\n\n"""


    slow_print(text_1)
    
    choices = ["Turn the light on", "leave the room"]
 
    
    player_choice = player_input(choices, decision_beer=0)
    if player_choice == 1:
        switch_light_on()
    if player_choice == 2:
        leave_room()
    
 
     
def switch_light_on():
    text_2 = f"""
    Ooopss the light switch isn't working and the windows are
    dyed in Black, so that there is no daylight in the room...\n\n"""
                
    slow_print(text_2)
    
    
    choices = ["Stay in the room", "Leave the room"]
    
    player_choice = player_input(choices, decision_beer=0)
    if player_choice == 1:
        search_the_key()

    if player_choice == 2:
        leave_room()
    
    
def search_the_key():
    
    text_3 = f"""
    ****** SUDDENLY *****  
    {game.name} starts to hear strange noises...
    The projector goes on and there's a new task!\n"""

    text_4 = ["""
                            ███████ ██ ███    ██ ██████  
                            ██      ██ ████   ██ ██   ██ 
                            █████   ██ ██ ██  ██ ██   ██ 
                            ██      ██ ██  ██ ██ ██   ██ 
                            ██      ██ ██   ████ ██████ """, 
                        
                            """
                            ████████ ██   ██ ███████ 
                               ██    ██   ██ ██      
                               ██    ███████ █████   
                               ██    ██   ██ ██      
                               ██    ██   ██ ███████  """ ,                

    """
    ██████   ██████  ████████ ████████ ██      ███████       ██   ██ ███████ ██    ██ 
    ██   ██ ██    ██    ██       ██    ██      ██            ██  ██  ██       ██  ██  
    ██████  ██    ██    ██       ██    ██      █████   █████ █████   █████     ████   
    ██   ██ ██    ██    ██       ██    ██      ██            ██  ██  ██         ██    
    ██████   ██████     ██       ██    ███████ ███████       ██   ██ ███████    ██    
                                                                            
    """]
    
    slow_print(text_3)
    countdown(5)
    for i in text_4:
        print(i)
        time.sleep(1)
        
        
  
    choices = ["take a look in the cupboard",
               "open all the drawers",
               "maybe the trashcan?"]
    player_choice = player_input(choices, decision_beer=0)

    

    while  player_choice != 3:
        slow_print("\nsearching...\n")
        countdown(3)
        slow_print("\n\nNot found... Try harder...\n")

        choices = ["take a look in the cupboard",
                  "open all the drawers",
                  "maybe the trashcan?"]
        player_choice = player_input(choices, decision_beer=0)

    if player_choice == 3:
        slow_print("\nsearching...\n")
        countdown(3)
        slow_print(f"\n\n{game.name} found the bottle key :)\n")
        ascii_output("bottle-key.txt", delay=True)
                             
        game.inventory += ["bottle-key"]
        slow_print(f"""
        {game.name} may leave this room now!
        Maybe back to the faculty room to drink a beer?""")
        leave_room()
                     
def leave_room():
    game.visited_rooms +=["closed_room_first_floor"]
    pass


# just for testing 
if __name__ == "__main__":
    class Game:
        def __init__(self):
            self.inventory = ["Stundenausweis"]
            self.events = []
            self.drunken = False
            self.name = 'lisa'
            self.visited_rooms = []

    game = Game()
    closed_room_first_floor(game)