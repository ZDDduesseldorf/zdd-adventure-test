from zdd_adventure.graphics import delayed_print_output




# 3 funktionality's in lecture hall: ( room_basement_1)

# 1.search for the light switch
# 2.look for more evidence
# 3.leave the room

def search_light_switch():
    text_pattern_2 = f'''
    Slowly {game.name} stands up. Since the room is so extremely dark, it's very clever to try to turn on the light.
    As always, the light switch is near the door. {game.name} still needs much longer than usual for the short way.
    Completely understandable, considering its condition.
    {game.name} stands with wobbly legs in front of the light switch and presses the switch.

    ......[click]...........


    {game.name} is lucky.
    It seems like the power is working without a band, as the room is now shining in a rather bright light.

    What does {game.name} want to do? '''
    delayed_print_output(text_pattern_2)
    player_choice = int(input('''
    1. search the teachers desk for more informations
    2. leave the room
    '''))
    #game.make_choice(choices)

    if player_choice == 1:
        find_evidence()

    if player_choice == 2:
        leave_room()
    else:
        "Choise has to be 1,2 or 3."
        player_choice

def find_evidence():
    player_choice = 0
    text_pattern_3 = f'''
    At first {game.name} looks around slowly.
    {game.name} get´s an idea. Maybe there are more clues on the desk....
    So {game.name} starts walking slowly to the teachers desk.
    When {game.name} arrives at the desk, he finds an almost empty desk. There are only the following items on the desk.

        -> A water bottle that has been started
        -> A cross screwdriver
        -> A pack of colored board markers

        However, {game.name} only has room for one item.
    '''
    delayed_print_output(text_pattern_3)
    player_choice = int(input(f'''
    1. water bottle
    2. cross screwdriver
    3. colored board markers

    which item would {game.name} like to hold?
    '''))
    if player_choice == 1:
        print('water bottle picked up')
        game.inventory += ['water bottle']
        leave_room()

    if player_choice == 2:
        print('cross screwdriver picked up')
        game.inventory += ['screwdriver']
        leave_room()

    if player_choice == 3:
        print('board markers picked up')
        game.inventory += ['board markers']
        leave_room()
    else:
        "Choise has to be 1,2 or 3."
        player_choice

def leave_room():
        txt = f'''
        {game.name} has left the lecture hall and is now standing in the corridor.
        {game.name} is just standing there, wondering what to do next.
        '''
        delayed_print_output(txt)










# main funktion for LECTURE HALL
def room_basement_1(game):
    ''' wake up in the lecture hall '''
    text_pattern_1 = f'''
    {game.name} open their eyes very slow. All {game.name} can see is a blurred dark room.
    After a certain amount of time {game.name} is able to find out where he is currently located.
    {game.name} is in the middle of his old lecture hall and {game.name} is really confused. {game.name} no longer understands
    the world.
    Why should {game.name} wake up in the old lecture hall of his old university?
    For {game.name} this all makes no sense.
    No matter how hard their tries to remember, {game.name} doesn't remember anything at all.

    {game.name} is just trying to keep calm and think about what
    options he has to find out what happened...


    '''

    delayed_print_output(text_pattern_1)
    player_choice = int(input(f'''
    1. search the teachers desk for any informations
    2. search for the light switch to find out if there is power
    3. leave the room as fast as {game.name} can
    '''))

    if player_choice == 1:
        find_evidence()

    if player_choice == 2:
        search_light_switch()

    if player_choice == 3:
        leave_room()
    else:
        "Deine Antwort muss 1, 2 oder 3 lauten."
        player_choice
    game.visited_rooms += ['lecture hall']



if __name__ == "__main__":
    class Game:
        def __init__(self):
            self.inventory = []
            self.events = []
            self.drunken = False
            # Playername query
            self.name = input(str('name:  '))
            self.visited_rooms = []

    game = Game()
    room_basement_1(game)
