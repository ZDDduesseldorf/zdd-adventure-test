from zdd_adventure.graphics import delayed_print_output




# 3 funktionality's in lecture hall: ( room_basement_1)

# 1.search for the light switch
# 2.look for more evidence
# 3.leave the room

def search_light_switch():
    text_pattern_2 = f'''
    Langsam steht {game.name} auf.
    Der Lichtschalter befindet sich Nade der Tür, sodass es nur 5 Meter sind. 
    {game.name} steht mit wackeligen Beinen auf um den Lichtschalter zu betätigen.
    
    ......[click]...........
    
    
    "Immerhin funktioniert der Strom noch.", dachte sich {game.name}.
    
    Der Raum ist jetzt beleutet.
    Was möchtest du tun? '''
    delayed_print_output(text_pattern_2)
    player_choice = int(input('''
    1. Umsehen nach Anhaltszeichen
    2. Raum verlassen
    '''))
    #game.make_choice(choices)

    if player_choice == 1:
        find_evidence()

    if player_choice == 2:
        leave_room()
    else:
        "Deine Antwort muss 1 oder 2 lauten."
        player_choice
              
def find_evidence():
    player_choice = 0
    text_pattern_3 = f'''
    {game.name} beginnt sich langsam Richtung Vorlesungspult zu begeben. Vielleicht liegen dort Hinweise...
    Als {game.name} am Pult ankommt, liegen folgende Items auf dem Pult.
    
    -> Eine angefangene Wasserflasche
    -> Ein Schraubenzieher
    -> Ein Packet Boardmarker
    
    {game.name} hat jedoch nur Platz für ein Item. 
    '''
    delayed_print_output(text_pattern_3)
    player_choice = int(input(f'''
    1. Wasserflasche
    2. Schraubenzieher
    3. Boardmarker
    
    Welches Item möchte {game.name} aufheben?
    '''))
    if player_choice == 1:
        print('Wasserflasche aufgehoben')
        game.inventory += ['Wasserflasche']
        leave_room()
        
    if player_choice == 2:
        print('Schraubenzieher aufgehoben')
        game.inventory += ['Schraubenzieher']
        leave_room()
        
    if player_choice == 3:
        print('Boardmarker aufgehoben')
        game.inventory += ['Boardmarker']
        leave_room()
    else:
        "Deine Antwort muss 1, 2 oder 3 lauten."
        player_choice
        
def leave_room():
        txt = f'''
        {game.name} hat den Vorlesungssaal jetzt wieder verlassen und steht jetzt auf dem Flur. 
        {game.name} steht nur da und fragt sich, wie es weiter gehen soll. 
        '''
        delayed_print_output(txt)










# main funktion for LECTURE HALL
def room_basement_1(game):
    ''' wake up in the lecture hall '''
    text_pattern_1 = f''' 
    {game.name} macht langsam die Augen auf. Sie lassen sich nur sehr langsam öffnen...
    Langsam aber sicher erkennt {game.name} die Umgebung wieder. Es ist die Hochschule. 
    Niemand weiß, wie {game.name} dort hingekommen war, doch jetzt ist {game.name} hier...
    Aber was soll {game.name} jetzt machen? Der Kopf ist völlig leer:
    ?...
    
    '''

    delayed_print_output(text_pattern_1)
    player_choice = int(input('''
    1. Umsehen nach Anhaltszeichen
    2. Lichtschalter suchen
    3. Raum verlassen
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
            self.inventory = ["Stundenausweis"]
            self.events = []
            self.drunken = False
            # Playername query
            self.name = input(str('name:  '))
            self.visited_rooms = []
                       
    game = Game()
    room_basement_1(game)
