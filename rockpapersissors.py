import os
import time
import random 
 
def add_entity(beats, new_entity):
    if new_entity not in beats:
        beats[new_entity] = []  # Creates a new key in the dictionary
    
    # Get list of existing entities (excluding the new one to avoid duplicate questions)
    existing_entities = [entity for entity in beats.keys() if entity != new_entity]
    
    for entity in existing_entities:
        choice = input(f"Does {new_entity} beat {entity}? (y/n): ").lower()
        if choice == 'y':
            beats[new_entity].append(entity)
        
        choice = input(f"Does {entity} beat {new_entity}? (y/n): ").lower()
        if choice == 'y':
            beats[entity].append(new_entity)

def exit_game():
    print('Thank you for playing!\n')
    print("Exiting", end="", flush=True)
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.55)
    print()  # This prints a new line
    exit()

# Dictionary for the game
# We store the values as lists so we can append new entities if the player wants to add new ones into the game
beat = {
    "rock": ["scissors"], 
    "paper": ["rock"],
    "scissors": ["paper"]
}

while True:
    try:
        os.system('clear')
        print("-" * 50)
        print("\t\tWelcome to the rock paper scissors game\t\t\n")
        print("Enter your choice:\n")
        print("1- Play\n")
        print("2- Creator Mode\n")
        print("3- Exit\n")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                os.system('clear')
                want_to_play_again = True
                while want_to_play_again:
                    os.system('clear')
                    choices = list(beat.keys())

                    print("Enter your choice: [", end="")
                    print(", ".join(choices), end="")
                    print("]")
                            
                    pc_choice = random.choice(choices)
                    p_choice = input("Player1 enter your choice: ").lower()
                 
                    if p_choice not in choices:
                        print("Invalid Choice")
                        time.sleep(2)
                        continue  # Continue the game instead of exiting
                    
                    print(f"You chose {p_choice} and the computer chose {pc_choice}")
                    
                    if p_choice == pc_choice:
                        print("Draw!")
                    elif pc_choice in beat.get(p_choice, []):
                        print("You WON!")
                    elif p_choice in beat.get(pc_choice, []):
                        print("Computer WON!")
                    else:
                        print("No clear winner - need more rules!")
                       
                    replay = input("Do you want to play again? (y/n): ").lower()
                    if replay == 'n':
                        want_to_play_again = False
                        

            case 2:
                os.system('clear')
                print("*" * 50)
                print("Welcome to the creator mode!")
                print("You can add NEW MOVES!")
                print("Available options:")
                choices = list(beat.keys())
                print(choices)
                print("*" * 50)
                new_entity = input("Enter the new entity: ").lower()
                
                if new_entity in beat:
                    print("Entity already exists!")
                    time.sleep(2)
                else:
                    print("Let's set the new rules")
                    add_entity(beat, new_entity)
                    print("Success!")
                    time.sleep(2)
                    
            case 3:
                os.system('clear')
                exit_game()
                
            case _:
                print("Invalid option!")
                time.sleep(1)
                continue

    except ValueError:
        print("Please enter a valid number!")
        time.sleep(1)
        continue
    except KeyboardInterrupt:
        print("\n\nGame interrupted!")
        exit_game()