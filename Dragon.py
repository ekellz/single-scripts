# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.


# Start loop
# User input to pick left or right door
# If left, user input to stay or go back
# If stay, user input to look around
# If look around, user input to take sword or leave

import random
import json
from pathlib import Path
import requests

# The Game
def save_game_state_data():
    """
    Save the current game state data to a JSON file.

    The game state data includes user choices and the equipment list.
    """
    game_state_data = {
        'user_choice': list(user_choice),
        'equipment_list': equipment_list
    }
    with open('game_state_data.json', 'w') as file:
        json.dump(game_state_data, file)

def prep_game_state():
    """
    Prepare the game state by loading it from a JSON file if it exists.

    If the file does not exist, initialize an empty game state.

    Returns:
        tuple: A tuple containing the user choices (set) and the equipment list (list).
    """
    if Path('game_state_data.json').exists():
        with open('game_state_data.json', 'r') as file:
            game_state_data = json.load(file)
            user_choice = set(game_state_data['user_choice'])
            equipment_list = game_state_data['equipment_list']
    else:
        user_choice = set()
        equipment_list = []
    return user_choice, equipment_list

def prepare_game_state():
    """
    Prepare the lists by reading data from a file and splitting it into two lists.

    Returns:
        tuple: A tuple containing two lists.
    """
    list1 = []
    list2 = []
    file_path = Path('/Users/ericajansen/Documents/Coding Projects/single-scripts/2024 Advent of Code/01_list.txt')
    with file_path.open('r') as file:
        for line in file:
            columns = line.split()
            if len(columns) > 1:
                list1.append(int(columns[0]))
                list2.append(int(columns[1]))
    return list1, list2

def end_game_session():
    """
    End the game session by saving the current game state to a file.
    """
    game_state = prepare_game_state()
    save_game_state_data(game_state)
    print("Game state saved.")

opponents = ["an angry ogre", "a hungry troll", "a fierce goblin", "a giant spider", "an evil sorceress", 
            "a scary ghost", "a hungry vampire", "a fierce werewolf", "a giant snake", "a wicked wizard", "a scary zombie", 
            "a fierce minotaur", "a giant cyclops", "a wicked warlock", "a scary banshee", "a hungry hydra", 
            "a fierce basilisk", "a giant griffin", "a wicked wraith", "a fierce sphinx", "a giant kraken", "a scary harpy", 
            "a hungry wyvern", "a fierce phoenix", "a wicked pegasus", "a scary centaur", "a hungry satyr", "a fierce dryad"]

# Name and Intro
name = input("Please type in your name ")

if len(name) < 2 or len(name) > 12:
    print("Please enter a name of at least 2 characters and not to exceed 12 characters. ")
    name = input("Please type in your name. ")
else:
# Generate a random name
    name_min_len = 2
    name_max_len = 12
    URL = f"https://uzby.com/api.php?min={name_min_len}&max={name_max_len}"

    response = requests.get(URL)
    handle = response.text

    translation_url = f"https://api.funtranslations.com/translate/quenya.json"
    text_to_translate = f"May the odds ever be in your favor."
    data = {
        'text': text_to_translate
    }

    translation_response = requests.post(translation_url, data=data)
    translation_result = translation_response.json()
    quenya_statement = translation_result.get('contents', {}).get('translated')

    if quenya_statement:
        print(f"Welcome to my dragon game, {name}! Your handle is {handle}. {quenya_statement}. Or, as you may know in the common tongue: may the odds ever be in your favor!  :) ")
    else:
        print(f"Welcome to my dragon game, {name}! Your handle is {handle}. May the odds ever be in your favor! ")

# The choices
left_door = "left"
right_door = "right"
stay = "stay"
back = "go back"
yes = "yes"
no = "no"

has_sword = False
user_choice = set()
equipment_list = []

while True:
    door_choice = input("You are on an adventure! You come across three doors. Would you like to choose the left, middle, or right door? ")
    user_choice.add(('door_choice', door_choice))

    # Left
    if door_choice == left_door:
        stay_or_go_back = input("You have chosen the left door. Would you like to go back or stay? (please type in your response exactly) ")
        user_choice.add(('stay_or_go_back', stay_or_go_back))
        if stay_or_go_back == stay:
            look_around_option = input("Well, now that you're here, would you like to look around? Type yes or no. ")
            user_choice.add(('look_around_option', look_around_option))
            if look_around_option == yes:
                sword_option = input("Welcome to this room! As you look around, you see a sword. "
                                     "Would you like to take ownership of it? Please type yes or no. ")
                user_choice.add(('sword_option', sword_option))
                if sword_option == yes:
                    key_option = input("Great choice! You now have the sword. When you pick up the sword, you notice a key. Would you like to take it? ")
                    has_sword = True
                    equipment_list.append('sword')
                    user_choice.add(('key_option', key_option))
                    if key_option == yes:
                        equipment_list.append('key')
                        print("You now have the sword and the key. ")
                else:
                    print("Welp, sorry to hear that, but off you go to the main area! ")
            else:
                print("Welp, back you go to the main area then! ")
        else:
            print("You chose not to stay, so you are being returned to the main area. ")
    
    # Middle
    elif door_choice == "middle":
        food_option = input("You chose the middle door. You look around and see a table with various items. Upon further inspection," 
                "you see a bag of bread and cheeses. Would you like to take it? Please type 'yes' or 'no' for your answer. ")
        user_choice.add(('food_option', food_option))
        if food_option == "yes":
            equipment_list.append('food')
            print("You now have the food. ")
        else:
            print("You chose not to take the food. ")

        # Closet door option
        closet_option = input("You see a closet door. Would you like to open it? Please type 'yes' or 'no' for your answer. ")
        user_choice.add(('closet_option', closet_option))
        if closet_option == "yes":
            print("You open the closet door and find a chest. You open the chest and find a key. You now have the key. ")
            equipment_list.append('key')
        else:
            print("You chose not to open the closet door. ")   

        # Opponent encounter
        opponent = random.choice(opponents)
        print(f"You hear a noise and turn around to see {opponent}! ")
        fight_option = input("Would you like to fight the opponent? Please type 'yes' or 'no' for your answer. ")
        user_choice.add(('fight_option', fight_option))
        if fight_option == "yes":
            print("You chose to fight the opponent! ")
            if equipment_list:
                print("You have the sword to defeat the opponent. Congratulations, you lived to move on your adventure and return to the beginning. ")
    
            else:
                print(f"So sorry, but {opponent} was too strong and you lost the game.  ")
                break
        else:
            print("You chose not to fight the opponent. ")

    # Right      
    else:
        stay_or_go_back = input("You chose the room on the right and oh my! There is a dangerous dragon here!"
                                "Would you like to stay or go back? Please type 'stay' or 'go back' for your answer. ")
        if stay_or_go_back == stay:
            fight_dragon_option = input("You brave soul! You decided to stay. Would you like to fight the dragon? "
                                       "Please type 'yes' or 'no' to indicate your answer. ")
            user_choice.add(('fight_dragon_option', fight_dragon_option))
            if fight_dragon_option == yes:
                print("You chose to fight the dragon! ")
                if has_sword:
                    print("You have the sword to defeat the dragon. Congratulations, you won the game! ")
                    break
                else:
                    print("So sorry, but the dragon was too big and dangerous. You lost your inventory of items. ")
                    equipment_list.clear()
                    break
            else:
                print("You chose wisely and did not fight the dragon without any weapons! ")
        else:
            print("Okay, you are back at the beginning. ")

# Example of how you might call end_game_session at the end of your game loop
# (This should be placed where your game loop ends)
end_game_session()
print("Game over! Thanks for playing! ")