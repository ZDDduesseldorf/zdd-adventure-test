# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 14:57:58 2022

@author: Miriam
"""
import random


choices = ["Run", "Switch on the light", "Do nothing"] #dummy input for presentation purposes


def player_input(choices, decision_beer=0): #choices: possible decisions/choices in a situation, type should be an array
                                            #decision_beer: value of 1 or 0, depending if the Player is drunk or not
    for i, choice in enumerate(choices): #loop for printing the different deciscions from the decision-array
        print(f"{i + 1}.  {choice}")
        
    player_choice_str=input("Decide! ") #player_choice: number the player chose on the keyboard
    
    if player_choice_str.isdigit(): #checks if the user has entered a digit
        player_choice=int(player_choice_str)
        
    else: #if the input is not a digit, the player is informed that he needs to type in another value 
        print("No valid input. Please select one of the offered choices by pressing the corresponding numbers on the keyboard. \n")
        return player_input(choices, decision_beer) #the PlayerInput function is called again
        
    
    if player_choice <= len(choices) and player_choice > 0: #to verify that the number typed in by the Player is not higher than the actual number of decisions/choices
        verified_input = player_choice
       
        if decision_beer == 1: #check if Player is drunk
            verified_input=random.randint(1, len(choices)) #if Player is drunk, select random answer from possible decisions
    
        if verified_input != player_choice: #Print statement to inform the player that his choice has been changed due to being drunk
            print("You're drunk and chose: ", verified_input)
        else:
            print("You chose: ", choices[verified_input-1])
        
        return verified_input #after checking it is valid, the Player's input is returned
         
    
    else: #if the input is not valid, the player is informed that he needs to type in another value 
        print("No valid input. Please select one of the offered choices by pressing the corresponding numbers on the keyboard. \n")
        return player_input(choices, decision_beer) #the PlayerInput function is called again
        

#print(player_input(choices,decision_beer=0))


while True:
    player_input(choices,decision_beer=0) 