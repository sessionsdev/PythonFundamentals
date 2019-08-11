'''
Code a game of rock paper scissors.

'''
import random

def get_hand(hand):
    if hand == 0:
        return "scissor"
    elif hand == 1:
        return "rock"
    elif hand == 2:
        return "paper"
    else:
        return "Invalid"


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





player_input = int(input("Please pick a number, 0 for Scissors, 1 for Rock, 2 for Paper: "))

computer_choice = random.randint(0, 2)

player_hand = get_hand(player_input)

computer_hand = get_hand(computer_choice)

winner = determine_winner(computer_hand, player_hand)


print(f"You picked {player_hand} and the computer picked {computer_hand}.")
print(winner)