from zdd_adventure.classes import name, delayed_print_output


# maybe we can create a file within all text pattern for room basement 1 (lecture hall )
# but not nessesary
    
#Storytext - just a first example
text_pattern_1 = f''' 
    {name} macht langsam die Augen auf. Sie lassen sich nur sehr langsam öffnen...
    Langsam aber sicher erkennt {name} die Umgebung wieder. Es ist die Hochschule. 
    Niemand weiß, wie {name} dort hingekommen war, doch jetzt ist {name} hier...
    Aber was soll {name} jetzt machen? Der Kopf ist völlig leer:
    ?...
    
    '''
text_pattern_2 = f'''
    Langsam steht {name} auf.
    Der Lichtschalter befindet sich Nade der Tür, sodass es nur 5 Meter sind. 
    {name} steht mit wackeligen Beinen auf um den Lichtschalter zu betätigen.
    
    ......[click]...........
    
    
    "Immerhin funktioniert der Strom noch.", dachte sich {name}.
    
    Der Raum ist jetzt beleutet.
    Was möchtest du tun? '''
              
text_pattern_3 = f'''
    {name} beginnt sich langsam Richtung Vorlesungspult zu begeben. Vielleicht liegen dort Hinweise...
    Als {name} am Pult ankommt, liegen folgende Items auf dem Pult.
    
    -> Eine angefangene Wasserflasche
    -> Ein Schraubenzieher
    -> Ein Packet Boardmarker
    
    {name} hat jedoch nur Platz für ein Item. 
    '''






# 3 funktionality's in lecture hall: ( room_basement_1)

# 1.search for the light switch
# 2.look for more evidence
# 3.leave the room

def search_light_switch(name, text_pattern_2):
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
    delayed_print_output(text_pattern_3)
    player_choice = int(input(f'''
    1. Wasserflasche
    2. Schraubenzieher
    3. Boardmarker
    
    Welches Item möchte {name} aufheben?
    '''))
    if player_choice == 1:
        print('Wasserflasche aufgehoben')
        leave_room()
        
    if player_choice == 2:
        print('Schraubenzieher aufgehoben')
        leave_room()
        
    if player_choice == 3:
        print('Boardmarker aufgehoben')
        leave_room()
    else:
        "Deine Antwort muss 1, 2 oder 3 lauten."
        player_choice
        
def leave_room():
        txt = f'''
        {name} hat den Vorlesungssaal jetzt wieder verlassen und steht jetzt auf dem Flur. 
        {name} steht nur da und fragt sich, wie es weiter gehen soll. 
        '''
        delayed_print_output(txt)










# main funktion for LECTURE HALL
def room_basement_1(name, text_pattern_1,text_pattern_2, text_pattern_3):
    ''' wake up in the lecture hall '''

    delayed_print_output(text_pattern_1)
    player_choice = int(input('''
    1. Umsehen nach Anhaltszeichen
    2. Lichtschalter suchen
    3. Raum verlassen
    '''))

    if player_choice == 1:
        find_evidence()

    if player_choice == 2:
        search_light_switch(name,text_pattern_2)

    if player_choice == 3:
        leave_room()
    else:
        "Deine Antwort muss 1, 2 oder 3 lauten."
        player_choice







room_basement_1(name, text_pattern_1,text_pattern_2, text_pattern_3)

