import os
import time
import random 
 
def add_entity(beats, new_entity):
    if new_entity not in beats:
        beats[new_entity] = [] # Creates a new  key in the dictionary
    for entity in beats:
        choice = input(f"Does {new_entity} beats {entity} ? (y/n)")
        if choice == 'y':
            beats[entity].append(new_entity)
        choice = input(f"Does {entity} beats {new_entity} ? (y/n)")
        if choice == 'y':
            beats[new_entity].append(entity)
        if entity == new_entity:
            break
            
    

def exit_game():
    print('Thank you for playing!\n')
    print("Exiting", end="", flush = True)
    for i in range(0,3):
        print(".", end="", flush = True)
        time.sleep(0.55)
    print() # This prints a new line
    exit()

# dictionarry for the game
# We store the values as lists so we can append new entities if the player wants to add new ones into the game
beat = {
    "rock": ["paper"], 
    "paper": ["scissors"],
    "scissors": ["rock"]
        }

while(True):
    os.system('clear')
    print("-"*50)
    print("\t\tWelcome to the rock paper scissors game\t\t\n")
    print("Enter your choice :\n")
    print("1- Play\n")
    print("2- Creator Mode\n")
    print("3- Exit\n")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            os.system('clear')
            WantToPlayAgain = True;
            while(WantToPlayAgain == True):
                os.system('clear')
                choices = list(beat.keys())

                print("Enter your choice : ", end="")
                print("[", end="")
                print(",".join(i for i in choices), end="")
                print("]", end="")
                        
                pc_choice = random.choice(choices)
                p_choice = input("\nPlayer1 enter your choice: ").lower()
             
                if p_choice not in choices:
                    print("Invalid Choice")
                    exit_game()
                
                if p_choice == pc_choice:
                    print(f"You both chose {pc_choice}")
                    print("Draw")
                elif p_choice in beat.get(pc_choice, []):
                    print(f"You chose {p_choice} and the computer chose {pc_choice}")
                    print("Human WON!")
                elif pc_choice in beat.get(p_choice, []):
                    print(f"You chose {p_choice} and the computer chose {pc_choice}")
                    print("Computer WON")
                   
                replay =  input("Do you want to play again ? (y/n)")
                if(replay == 'n'):
                    exit_game()
                    

        case 2:
            os.system('clear')
            print("*"*50)
            print("Welcome to the creator mode!")
            print("You can add NEW MOVES!")
            print("Available options : ")
            choices = list(beat.keys())
            print(choices)
            print("*"*50)
            new_entity = input("Enter the new entity ").lower()
            print("lets set the new rules")
            add_entity(beat, new_entity)
            print("Sucess !")
        case 3:
            os.system('clear')

            exit_game()
        case  _:
            print("Invalid option!")
            continue



                
            
      
