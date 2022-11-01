def intro_Scene():
    print("Which room would you like to visit first?")
    decisions = ["Room_1","Room_2","Room_3"]
    userInput = ""
    while userInput not in decisions:
        print("Your options:\n a) Room_1\n b) Room_2\n c) Room_3")
        userInput = input().lower()
        if userInput == "a":
          show_Room_1()
        elif userInput == "b":
          show_Room_2()
        elif userInput == "x":
          show_Room_3()
        else: 
          print("Please enter a valid option.")

if __name__ == "__main__":
  while True:
    print("Welcome to the ZDDAdventure Game!")
    print("subtitle...")
    print("Presented by: DAISY")
    print("Let's start with your name: ")
    name = input()
    print("Good luck, " + name + ".")
    intro_Scene()
    
