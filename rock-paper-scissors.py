"""
take in a number 0-2 from the user that represents their hand
generate a random number 0-2 to use for the computer's hand
call the function get_hand to get the string representation of the user's hand
call the function get_hand to get the string representation of the computer's hand
call the function determine_winner to figure out who won
print out the player hand and computer hand
print out the winner
"""

import random

def get_hand(hand):
    # 0 = rock, 1 = paper, 2 = scissors
    if hand == 0:
        return "rock"
    elif hand == 1:
        return "paper"
    else:
        return "scissors"
    
def determine_winner(user_hand, computer_hand):
    # 0 = rock, 1 = paper, 2 = scissors
    if user_hand == computer_hand:
        return "It's a tie!"
    elif user_hand == 0 and computer_hand == 2:
        return "You win!"
    elif user_hand == 1 and computer_hand == 0:
        return "You win!"
    elif user_hand == 2 and computer_hand == 1:
        return "You win!"
    else:
        return "Computer wins!"
    
def main():
    user_hand = int(input("Enter a number (0 = rock, 1 = paper, 2 = scissors): "))
    computer_hand = random.randint(0, 2)
    
    print(f"You chose {get_hand(user_hand)}")
    print(f"The computer chose {get_hand(computer_hand)}")
    
    print(determine_winner(user_hand, computer_hand))