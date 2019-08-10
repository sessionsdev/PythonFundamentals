'''
Code a game of rock paper scissors.

'''
import random


# function to get hand based on number
# the function should take in a number and return the string representation of the hand
def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    if hand == 0:
        return "scissor"
    elif hand == 1:
        return "rock"
    elif hand == 2:
        return "paper"
    else:
        return "Invalid"

    # for example if the variable hand is 0, it should return the string "scissor"
    pass

# function should take in two hands and return a string "You won!" or "You lost :(" or "You tied!"
def determine_winner(computer, player):
    win = "You win!"
    lose = "You lose!"
    if computer == player:
        return "You tied!"
    elif computer == "scissor":
        if player == "rock":
            return win
        else:
            return lose
    elif computer == "rock":
        if player == "paper":
            return win
        else:
            return lose
    elif computer == "paper":
        if player == "scissor":
            return win
        else:
            return lose
    else:
        return "Invalid"



'''
Start here
'''

# take in a number 0-2 from the user that represents their hand
player_input = int(input("Please pick a number, 0 for Scissors, 1 for Rock, 2 for Paper: "))

# generate a random number 0-2 to use for the computer's hand
computer_choice = random.randint(0, 2)

# call the function get_hand to get the string representation of the user's hand
player_hand = get_hand(player_input)

# call the function get_hand to get the string representation of the computer's hand
computer_hand = get_hand(computer_choice)

# call the function determine_winner to figure out the winner
winner = determine_winner(computer_hand, player_hand)

# print out the player hand and computer hand
print(f"You picked {player_hand} and the computer picked {computer_hand}.")

# print out the winner
print(winner)