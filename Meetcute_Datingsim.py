
from zdd_adventure.graphics import delayed_print_output

def Meet_cute_dating_sim():
    name = input(str('name:  '))
    counter = []
    text_pattern = f'''
    {name} went to the second floor after his Poker game. Full of joy and happines that he won his Poker game,
    he encounter someone. There {name} saw a beautiful lil cute girl .{name} was astonished because the girl is so beautiful.
    {name} at first laked words but said to his self this girl can be his future wife. Then {name} got enough and
    decided to talk to the girl.'''
    print(text_pattern)
    delayed_print_output(text_pattern)
    player_choice = int(input(f'''
    1. Hey! I am {name} and you?
    2. Hey girl! What's your name?
    3. Hey girl why don't you sti-nog the number down for me?
    '''))
    if player_choice == 1:
        counter = counter + 5
        print("Celia: my name is Celia")
        
    if player_choice == 2:
        counter = counter + 5
        print("Celia: my name is Celia")
        
    if player_choice == 3:
        counter = counter + 0
        print("Celia: What the Hell?")
        
    #else:
        #"Your Answer must be 1, 2,or 3 "
        #player_choice
    #for choice in len(player_choice()):
        #print("my name is Celia")
        
    print(f"{name} goes further in the conversation")
    
    player_choice = int(input('''
    1. What are you doing here?
    2. You have a beautiful smile.
    3. Here I do not mean to disturb you, but I coulbn't resist and this could be my only chance. Can I ask you for your number?
    '''))
    
    if player_choice == 1:
        print("Celia: I'm just chilling and you?")
        print(f"{name}: I came to take some fresh air and dance a lil bit since a won a Poker game")
        
    if player_choice == 2:
        print("Celia: Hahahah!! Thanks. I am flattered")
        
    if player_choice == 3:
        print("Celia: Usually I do not give my number to unkwown person but you seem different. My number is +49 1579 4567890")
        
    else:
        print("Your Answer must be 1, 2,or 3 ")
        player_choice
        
Meet_cute_dating_sim()
  
#%%        
responses = ["Yes", "No", "Maybe", "I'm not sure"]
import random


def choose_response():
  response = input("Please choose a response: ")
  if response in responses:
    return response
  else:
    return random.choice(responses)

while True:
  response = choose_response()
  print(f"Simulator: {response}")

if response == "Yes":
  print("Simulator: Yay! I'm so glad you said yes!")
elif response == "No":
  print("Simulator: Oh no, why not?")

hobbies = ["I love playing video games", "I enjoy reading books", "I like to go on hikes"]
feelings = ["I'm feeling happy today", "I'm feeling a little sad", "I'm feeling confused"]

def choose_hobby_response():
  return random.choice(hobbies)

def choose_feeling_response():
  return random.choice(feelings)


choose_response()
choose_hobby_response()
choose_feeling_response()
    
    




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    