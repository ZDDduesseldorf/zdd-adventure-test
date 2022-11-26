from zdd_adventure.closed_room_first_floor import slow_list_print
from zdd_adventure.graphics import slow_print, countdown, ascii_output
from zdd_adventure.InputChecker_and_DrunkMode import player_input

whiteboard = ['T was here']

# WHITEBOARD ANPASSEN
#ascii_output("aktion_open_door.txt", True, 0.0003)
def lecture_hall(game):
    text_pattern = ['''
██      ███████  ██████ ████████ ██    ██ ██████  ███████ 
██      ██      ██         ██    ██    ██ ██   ██ ██      
██      █████   ██         ██    ██    ██ ██████  █████   
██      ██      ██         ██    ██    ██ ██   ██ ██      
███████ ███████  ██████    ██     ██████  ██   ██ ███████
                    ''','''
██   ██  █████  ██      ██      
██   ██ ██   ██ ██      ██      
███████ ███████ ██      ██      
██   ██ ██   ██ ██      ██      
██   ██ ██   ██ ███████ ███████ 
                    ''']
    slow_list_print(text_pattern, delay=1)
    slow_print(f'{game.name} open their eyes very slow.'+2*'\n')
    countdown(4) 
    print( '\n')
    slow_print(f'All {game.name} can see is a blurred dark room.'+2*
                         '\n'
                         +f'After a certain amount of time {game.name} is able to find out where he is currently located.'
                         +'\n')
    enter = input('### press enter ### \n')
    enter
    slow_print(f'{game.name} is in the middle of their old lecture hall.' +'\n'
                         + f'{game.name} no longer understands the world... \n')
    slow_print(f'''Just trying to keep calm and think about what
options {game.name} has to find out what happened...''')
    enter
    choices = ['go to teachers desk','go to student chair rows', 'leave the room']
    print( '\n')
    choise = player_input(choices, decision_beer=0)
    
    enter
    if choise == 1:
        teachers_desk(whiteboard)
    if choise == 2:
        chair_rows()
    if choise == 3:
        leave_room()
    
def leave_room():
    '''
    two ways possible to leave the lecture hall. 
    Directly by exit-door or by exit-door but before visiting the storage room.
    '''
    def storage_room():
        '''
        Side door room bevor leaving the lecture hall.
        To open the door its nessesarry to find the storage room key by the chair rows.
        '''
        slow_print(f'{game.name} slowly goes to the storage room door ...')
        countdown(3)
        print('\n')
        
        # Query if storage room key is in invenrory
        
        if 'storage room key' in game.inventory:
            slow_print('''The storage room is open now. The room is very small. 
Unfortunately nothing to find here besides a disinfectant bottle''')
            game.inventory += ['disinfectant bottle']
            enter =  input('### press enter ### \n')
            slow_print(f'{game.name} is now leaving the lecture hall with his disinfectant bottle...')
            countdown(5)
            game.visited_rooms += ['lecture hall']
            enter 
        else:
            slow_print(f'ohh noo, {game.name} need the storage room key to open the door.')
            enter = input('### press enter ### \n')
            enter
            slow_print(f'{game.name} is now leaving the lecture hall...')
            countdown(5)
            game.visited_rooms += ['lecture hall']
            enter
    
    # leaving the lecture hall
    print('\n')
    slow_print(f'Now {game.name} will leave the lecture hall')
    enter =  [input('### press enter ### \n')]
    countdown(3)
    print('\n')
    slow_print(f'''ohhh wait, whats this? Another door? 
{game.name} found a storage room door.  \n ''')
    slow_print(f'For leaving the room which door should {game.name} choose?')
    choises = ['storage room door','exit door']
    # 2 possible ways for leaving
    choise = player_input(choises, decision_beer=0)
    if choise == 1:
        storage_room()
    if choise == 2:
        slow_print(f'{game.name} is now leaving the lecture hall...')
        countdown(5)
        enter


def teachers_desk(whiteboard):
    '''
    '''
    
    def look_at_whiteboard(whiteboard):
        ### ASCI Art Pic missing
        countdown(3)
        print('\n')
        print(game.whiteboard)
        print('\n')
        
    def write_on_whiteboard(whiteboard):
        if 'Whiteboard marker' in game.inventory:
            entry = str(input(f'What does {game.name} want to add on the  whiteboard \n'))
            game.whiteboard += [entry]
            print('\n gespeichert')
            return whiteboard
        
        else:
            slow_print(f'Ohhh noo, {game.name} missed to pick up the boardmarker.')
            
    
########################################## teachers desk

    slow_print(f'Now {game.name} search the teachers desk for more informations.')
    print('\n')
    countdown(6)
    print('\n')
    slow_print(f'''{game.name} has found three things on the teeachers desk. 
{game.name} only can pick up ONE Item''')                                                 #grammatik ???????
    enter = input('### press enter ### \n')    
    slow_print('''--> Whiteboard marker
               
--> The DAISY degree documentaion

--> A party flyer from the Media Faculty
    ''')
    slow_print(f'What does {game.name} want to pick up? \n')
    choises = ['Whiteboard marker','The DAISY degree documentaion','A party flyer from the Media Faculty']
    choise = player_input(choises,decision_beer=0)
    if choise == 1:
        slow_print('Whiteboard marker picked up.')
        game.inventory += ['Whiteboard marker']
    if choise == 2:
        slow_print('DAISY degree documentaion picked up.')
        game.inventory += ['The DAISY degree documentaion']
    if choise == 3:
        slow_print('Party flyer from the Media Faculty picked up.')
        game.inventory += ['A party flyer from the Media Faculty']
        
########################################## whiteboard
    print('\n')
    enter
    print('\n')
    slow_print(f'''Because {game.name} is so close to the whiteboard right know {game.name} recognize 
that something is written there.
               ''')
    print('\n')
    enter =  [input('### press enter ### \n')]
    ready_to_leave = True
    while ready_to_leave == True:
        enter
        slow_print(f'What does {game.name} want to do?')
        choises = ['look at the whiteboard', 'write something on the board','leave the room']
        choise = player_input(choises, decision_beer=0)
        # WHITEBOARD ALS BILD EINGEBEN
        whiteboard = ['Hello there. XD was here. Just for your information ']
        

        if choise == 1:
            look_at_whiteboard(whiteboard)
        if choise == 2:
            write_on_whiteboard(whiteboard)
            print('Whiteboard: \n' )
            for i,y in enumerate(whiteboard):
                print(whiteboard[i], y) 
                
        if choise == 3:
            return ready_to_leave == True
            
        leave_room()
    

    
        
def chair_rows():
    '''
    '''
    def chair_row_1():
        slow_print(f'{game.name} is wakling through all seats from the first chair row.') 
        print('\n')
        countdown(6)
        print('\n')
        slow_print('Unfortunately nothing was found.')
        print('\n')
        slow_print(f'Now {game.name} has to choose again:')
        print('\n')
        choises_3 = ['search chair row 2', 'go back']
        choise = player_input(choises_3, decision_beer=0)
        if choise == 1:
            chair_row_2()
        if choise == 2:
            go_back()
            
    def chair_row_2():
        slow_print(f'{game.name} is wakling through all seats from the second chair row.') 
        print('\n')
        countdown(6)
        print('\n')
        slow_print(f'{game.name} finds a book with the title "gradient descent"...')
        countdown(3)
        game.inventory += ['book "gradient descent" ']
        print('\n')
        slow_print('Item: book "gradient descent" picked up')
        print('\n')
        slow_print(f'Now {game.name} has to choose again:')
        print('\n')
        choises_3 = ['search chair row 3', 'go back']
        choise = player_input(choises_3, decision_beer=0)
        if choise == 1:
            chair_row_3()
        if choise == 2:
            go_back()
        
    def chair_row_3():
        slow_print(f'{game.name} is wakling through all seats from the third chair row.') 
        print('\n')
        countdown(6)
        print('\n')
        slow_print('Unfortunately nothing was found.')
        print('\n')
        slow_print(f'Now {game.name} has to choose again:')
        print('\n')
        choises_3 = ['search chair row 4', 'go back']
        choise = player_input(choises_3, decision_beer=0)
        if choise == 1:
            chair_row_4()
        if choise == 2:
            go_back()
            
    def chair_row_4():
        slow_print(f'{game.name} is wakling through all seats from the fourth chair row... ')
        print('\n')
        countdown(6)
        print('\n')
        slow_print(f'{game.name} finds a special key. The key looks like a key for a storage room...')
        countdown(3)
        print('\n')
        game.inventory += ['storage room key']
        print('\n')
        slow_print('Item: key for storage room picked up')
        print('\n')
        slow_print(f'{game.name} searched all chair rows.... ')
        print('\n')
        go_back()
        
    def go_back():
        slow_print(f'{game.name} is back in the middle of the lecture hall now and ... ')
        countdown(3)
        leave_room()
        
    def relax():
        print('\n')
        slow_print(f'{game.name} sits down on the first chair and try to relax for some time. ')
        print('\n')
        countdown(10)
        print('\n')
        slow_print(f'What does {game.name} want to do now?')
        choises_2 = ['search chair row 1', 'go back']
        choise = player_input(choises_2, decision_beer=0)
        if choise == 1:
            chair_row_1()
        if choise == 2:
            go_back()
        
# Chair Rows
    slow_print(f'''
{game.name} is standing besides the student chair rows.
What does {game.name} want to do now?''')
    print('\n')
    choises_2 = ['sit down and relax for some time', 'search chair row 1']
    choise = player_input(choises_2, decision_beer=0)
    if choise == 1:
        relax()
            
    if choise == 2:
        chair_row_1()
        

        

        
        

if __name__ == "__main__":
    class Game:
        def __init__(self):
            self.inventory = []
            self.events = []
            self.drunken = False
            # Playername query
            self.name = input(str('name:  ')).upper()
            self.visited_rooms = []
            self.whiteboard = []

game = Game()
lecture_hall(game)
        
