# -*- coding: UTF-8 -*-
import random


def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "error"

def number_to_name(number):
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
    player_choice_name = number_to_name(player_choice)
    print("Player chooses"), player_choice_name
    comp_number = random.randrange(0, 5)
    comp_name = number_to_name(comp_number)
    print("Computer chooses"), comp_name
    if player_choice_name != "error":
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
