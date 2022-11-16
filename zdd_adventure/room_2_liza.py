# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:33:26 2022

@author: lizak
"""
from zdd_adventure.graphics import delayed_print_output
from zdd_adventure.graphics import countdown
import time
# the locked room on the 1st basement 

# the functionalities :
# input_check()
# closed_room_first_floor():
# switch_light_on():
# search_the_key()
# leave_room()


# checks if Player_choice is a valid number
def input_check(choice_list, txt):
    while True:
        #print(choice_list)
        player_choice = int(input("Choice: "))
        if player_choice in choice_list:
            #print("found")
            return player_choice
        else:
            print(txt)
    
    
    
def closed_room_first_floor(game):
    text_1 = f"""WoOoooOw the kiddo did it... 
        {game.name} is now in a new room, but can't see anything...
        it's dark
        """

    delayed_print_output(text_1)
    
 
    delayed_print_output('''
    1. Turn the light on
    2. leave the room
    ''')
    
    player_choice = input_check([1,2], "Decide between 1 or 2_ ")
    if player_choice == 1:
        switch_light_on()
    if player_choice == 2:
        leave_room()
    
 
     
def switch_light_on():
    text_2 = f"""
    Ooopss the light switch isn't working and the windows are 
    dyed in Black, so that there is no daylight in the room...\n\n
    """
                
    delayed_print_output(text_2)
    
    delayed_print_output("""
    The person has now the chance to decide:                          
    1. Stay in the room
    2. Leave the room
    """)
    player_choice = input_check([1,2],"""That number isn't valid...
                                Option 1 or 2?""")
    if player_choice == 1:
        search_the_key()

    if player_choice == 2:
        leave_room()
    
    
def search_the_key():
    
    text_3 = f"""
    ****** SUDDENLY *****  
    {game.name} starts to hear strange noises...
    The projector goes on and there's a new task!\n
    """

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
    
    delayed_print_output(text_3)
    countdown(5)
    for i in text_4:
        print(i)
        time.sleep(1)
        
        
    delayed_print_output("""
    1. take a look in the cupboard
    2. open all the drawers
    3. maybe the trashcan?
    """)
    
    player_choice = input_check([1,2,3],"""That number isn't valid...
                                Option 1, 2 or 3?""")

    while  player_choice != 3:
        delayed_print_output("searching...\n")
        countdown(3)
        delayed_print_output("\n\nNot found... Try harder...\n")
        delayed_print_output("""
        1. take a look in the cupboard
        2. open all the drawers
        3. maybe the trashcan?
           """)
        player_choice = input_check([1,2,3],"""That number isn't valid...
                                      Option 1, 2 or 3?""")
    if player_choice == 3:
        delayed_print_output("searching...\n")
        countdown(3)
        delayed_print_output(f"\n\n{game.name} found the bottle key :)\n")
        delayed_print_output("""
                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                             @@@@@@@@@@@& .,,,. &@@@@@@@@@@@
                             @@@@@@@&*,&@&*..,,%@@.*@@@@@@@@
                             @@@@@@@,,,@@@@@@@@@@@@,@@@@@@@@
                             @@@@@@@@ .*@@@,  &@@%..@@@@@@@@
                             @@@@@@@@@@....,,,...,@@@@@@@@@@
                             @@@@@@@@@@@@ .....,@@@@@@@@@@@@
                             @@@@@@@@@@@@@.....@@@@@@@@@@@@@
                             @@@@@@@@@@@@*.....,@@@@@@@@@@@@
                             @@@@@@@@@@@@.......@@@@@@@@@@@@
                             @@@@@@@@@@@@.  /...@@@@@@@@@@@@
                             @@@@@@@@@@@@.. (,, @@@@@@@@@@@@
                             @@@@@@@@@@@@.. (...@@@@@@@@@@@@\n\n""")
                             
        game.inventory += ["bottle-key"]
        delayed_print_output(f"""
        {game.name} may leave this room now!
        Maybe back to the faculty room to drink a beer?""")
        leave_room()
                     
def leave_room():
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
