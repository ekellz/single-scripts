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


# Intro
name = input("Please type in your name ")
print(f"Welcome to my dragon game, {name}! May the odds ever be in your favor! :) ")

# The choices
left_door = "left"
right_door = "right"
stay = "stay"
back = "go back"
yes = "yes"
no = "no"

has_sword = False

while True:
    door_choice = input("You have a choice. Pick a door: left or right! ")

    # Left
    if door_choice == left_door:
        stay_or_go_back = input("You have chosen the left door. Would you like to go back or stay? (please type in your response exactly) ")
        if stay_or_go_back == stay:
            look_around_option = input("Well, now that you're here, would you like to look around? Type yes or no. ")
            if look_around_option == yes:
                sword_option = input("Welcome to this room! As you look around, you a sword. "
                                     "Would you like to take ownership of it? Please type yes or no. ")
                if sword_option == yes:
                    print("Great choice! You now have the sword and are returning to the main area. ")
                    has_sword = True
                else:
                    print("Welp, sorry to hear that, but off you go to the main area! ")
            else:
                print("Welp, back you go the main area then! ")
        else:
            print("You chose not to stay, so you are being returned to the main area. ")
    # Right      
    else:
        stay_or_go_back = input("You chose the room on the right and oh my! There is a dangerous dragon here!"
                                "Would you like to stay or go back? Please type 'stay' or 'go back' for your answer. ")
        if stay_or_go_back == stay:
            fight_dragon_option = input("You brave soul! You decided to stay. Would you like to fight the dragon? "
                                       "Please type 'yes' or 'no' to indicate your answer. ")
            if fight_dragon_option == yes:
                print("You chose to fight the dragon! ")
                if has_sword:
                    print("You have the sword to defeat the dragon. Congratulations, you won the game! ")
                    break
                else:
                    print("So sorry, but the dragon was too big and dangerous. You lost, game over. ")
                    break
            else:
                print("You chose wisely and did not fight the dragon without any weapons! ")
        else:
            print("Okay, you are back at the beginning. ")

    


