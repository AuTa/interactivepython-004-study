# -*- coding: UTF-8 -*-
import random


def number_to_number(number):
    if number == "rock":
        return 0
    elif number == "Spock":
        return 1
    elif number == "paper":
        return 2
    elif number == "lizard":
        return 3
    elif number == "scissors":
        return 4
    else:
        return "error"

def number_to_number(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "error"

def rpsls(player_choice):
    player_choice_number = number_to_number(player_choice)
    print("Player chooses"), player_choice_number
    comp_number = random.randrange(0, 5)
    comp_number = number_to_number(comp_number)
    print("Computer chooses"), comp_number
    if player_choice_number != "error":
        result = (player_choice - comp_number) % 5
    else:
        print("This project is error.")
    if result == 1 or result == 2:
        print("Player wins!")
    elif result == 3 or result == 4:
        print("Computer wins!")
    elif result == 0:
        print("Player and computer tie!")
    else:
        print("This project is error.")
    print("")

rpsls(0)
rpsls(1)
rpsls(2)
rpsls(3)
rpsls(4)
rpsls(int(input("")))
