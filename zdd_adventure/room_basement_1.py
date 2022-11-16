from zdd_adventure.graphics import delayed_print_output
from zdd_adventure.graphics import countdown
import room_2_liza


# 3 funktionality's in lecture hall: ( room_basement_1)

# 1.search for the light switch
# 2.look for more evidence
# 3.leave the room
# ['''
# Slowly {game.name} stands up. Since the room is so extremely dark, it's very clever to try to turn on the light.
# As always, the light switch is near the door. {game.name} still needs much longer than usual for the short way.
# Completely understandable, considering its condition.
# {game.name} stands with wobbly legs in front of the light switch and presses the switch.

# ......[click]...........


# {game.name} is lucky.
# It seems like the power is working without a band, as the room is now shining in a rather bright light.

# What does {game.name} want to do? '''

# text_pattern_3 = f'''
# At first {game.name} looks around slowly.
# {game.name} get´s an idea. Maybe there are more clues on the desk....
# So {game.name} starts walking slowly to the teachers desk.
# When {game.name} arrives at the desk, he finds an almost empty desk. There are only the following items on the desk.

#     -> A water bottle that has been started
#     -> A cross screwdriver
#     -> A pack of colored board markers

#     However, {game.name} only has room for one item.
# '''

# text_pattern_1 = f'''
# {game.name} open their eyes very slow. All {game.name} can see is a blurred dark room.
# After a certain amount of time {game.name} is able to find out where he is currently located.
# {game.name} is in the middle of his old lecture hall and {game.name} is really confused. {game.name} no longer understands
# the world.
# Why should {game.name} wake up in the old lecture hall of his old university?
# For {game.name} this all makes no sense.
# No matter how hard their tries to remember, {game.name} doesn't remember anything at all.

# {game.name} is just trying to keep calm and think about what
# options he has to find out what happened...



#    game.visited_rooms += ['lecture hall']


def lecture_hall(game):
    delayed_print_output(f'{game.name} open their eyes very slow.'+2*'\n')
    countdown(4) 
    print( '\n')
    delayed_print_output(f' All {game.name} can see is a blurred dark room.'+2*
                         '\n'
                         +f'After a certain amount of time {game.name} is able to find out where he is currently located.'
                         +'\n')
    enter = input('### press enter ### \n')
    enter
    delayed_print_output(f'{game.name} is in the middle of his old lecture hall.' +'\n'
                         + f'{game.name} no longer understands the world.')
    delayed_print_output(f''' Just trying to keep calm and think about what
                         options {game.name} has to find out what happened...''')
    enter
    choise = input(delayed_print_output('''choose option:
          
          --> 1. go to teachers desk
          
          --> 2. go to student stair rows
          
          --> 3. leave the room
          '''))
    enter
    if choise == '1':
        pass
    if choise == '2':
        stair_rows()
    if choise == '3':
        pass
    
    
def stair_rows():
    choise = input(delayed_print_output(f'''
                   
            {game.name} is standing besides the student stair rows.
            
            What does {game.name} want to do now?
            
            --> 1. sit down and relax for some time
       
            --> 2. search stair row 1
                   
            '''))
    if choise == '1':
        pass
    if choise == '2':
        pass
    
    































if __name__ == "__main__":
    class Game:
        def __init__(self):
            self.inventory = []
            self.events = []
            self.drunken = False
            # Playername query
            self.name = input(str('name:  ')).upper()
            self.visited_rooms = []

    game = Game()
    lecture_hall(game)
