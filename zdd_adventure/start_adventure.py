"""This starts the adventure
"""
import zdd_adventure.save as save
import zdd_adventure.change_place as change_place

end_game = False

def start():
    for _ in range(5):
        print(20 * ">")
    print(">>>> Something awesome is about to happen...")
    for _ in range(5):
        print(20 * ">")
    print(">>>> Loading Data...")
    #spieldaten laden
    acc = save.load_data()
    accounts = list(acc.keys())
    my_game = ""
    while my_game == "":
        print("\n\nChoose your Game-stats\n\n0: New Game")
        for i in range(len(accounts)):
            print((i+1), accounts[i])
        my_game = input("\nInsert your Game:")
        if my_game.isnumeric():
            if not int(my_game) <= len(accounts):
                my_game = ""
        else:
            my_game = ""
    name = ""
    if my_game == "0":
        print("Welcome newcommer! \nFirst tell me your Name") # falls das in dritte form geschrieben werden soll bitte korrigieren
        while (name == "") or (name in accounts):
            name = input("Enter your name: ")
        save.create_new_player(name)
    else:
        name = accounts[(int(my_game)-1)]
        print(f'Welcome back {name}!')
    data = save.load_player_data(name)
    while not end_game:
        #change_place.room_action(data,"func")
        data = change_place.change_place(data)
        save.save_data(data)
    
    

start()