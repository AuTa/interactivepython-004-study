# -*- coding: UTF-8 -*-
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# http://www.codeskulptor.org/#save2_ge78pZ3jYY.py

import random
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# initialize global variables used in your code
range_now = 100


# helper function to start and restart the game
def new_game():
    global secret_number
    global remaining_number
    global range_now
    if range_now == 100:
        secret_number = random.randrange(0, 100)
        remaining_number = 7
    if range_now == 1000:
        secret_number = random.randrange(0, 1000)
        remaining_number = 10
    print("New game.Range is from 0 to %d\nNumber of remaining guesses is %d\n" % (range_now, remaining_number))


# define event handlers for control panel
def restart_game():
    # button that restarts
    new_game()


def range100():
    # button that changes range to range [0,100) and restarts
    global range_now
    range_now = 100
    new_game()


def range1000():
    # button that changes range to range [0,1000) and restarts
    global range_now
    range_now = 1000
    new_game()


def input_guess(guess):
    # main game logic goes here
    global remaining_number
    guess = int(guess)
    if guess < secret_number:
        remaining_number -= 1
        if remaining_number == 0:
            print("Guess was %d\nNumber of remaining guesser is %d\nYou ran out of guesses.The number was %d\n"
                  % (guess, remaining_number, secret_number))
            new_game()
        else:
            print("Guess was %d\nNumber of remaining guesser is %d\nHigher!\n" % (guess, remaining_number))
    if guess > secret_number:
        remaining_number -= 1
        if remaining_number == 0:
            print("Guess was %d\nNumber of remaining guesser is %d\nYou ran out of guesses.The number was %d\n"
                  % (guess, remaining_number, secret_number))
            new_game()
        else:
            print("Guess was %d\nNumber of remaining guesser is %d\nLower!\n" % (guess, remaining_number))
    if guess == secret_number:
        remaining_number -= 1
        print("Guess was %d\nNumber of remaining guesser is %d\nCorrect!\n" % (guess, remaining_number))
        new_game()
    pass


# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Restart game", restart_game, 200)
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game and start frame
new_game()
f.start()