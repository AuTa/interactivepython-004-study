# -*- coding: UTF-8 -*-
# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user31_AoRQJ6hJwt_2.py

# import simplegui
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")

# initialize some useful global variables
in_play = False
outcome = ['', '']
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)


# define hand class
class Hand:
    def __init__(self):
        self.list_card = []

    def __str__(self):
        str_hand = 'Hand contains'
        if len(self.list_card) > 0:
            for i in range(len(self.list_card)):
                str_hand = str_hand + ' ' + str(self.list_card[i])
        return str_hand

    def add_card(self, card):
        self.list_card.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        self.hand_value = 0
        list_rank = []
        for i in self.list_card:
            self.hand_value += VALUES[i.get_rank()]
            list_rank.append(i.get_rank())
        if 'A' in list_rank and self.hand_value + 10 <= 21:
            self.hand_value += 10
        return self.hand_value

    def draw(self, canvas, pos):
        for i in self.list_card:
            i.draw(canvas, pos)
            pos[0] = pos[0] + CARD_SIZE[0] + 20


# define deck class
class Deck:
    def __init__(self):
        self.list_card = []
        for i in SUITS:
            for j in RANKS:
                self.list_card.append(Card(i, j))

    def shuffle(self):
        # shuffle the deck
        return random.shuffle(self.list_card)

    def deal_card(self):
        return self.list_card.pop()

    def __str__(self):
        str_deck = 'Deck contains'
        for i in self.list_card:
            str_deck = str_deck + ' ' + str(i)
        return str_deck

# deck = Deck()
# dealer = Hand()
# player = Hand()

#define event handlers for buttons
def deal():
    global outcome, in_play, score, deck, dealer, player
    deck = Deck()
    dealer = Hand()
    player = Hand()
    deck.shuffle()
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    outcome[0] = ''
    outcome[1] = 'Hit or Stand?'
    if in_play:
        score -= 1
    in_play = True

def hit():
    global outcome, in_play, score
    if in_play:
        player.add_card(deck.deal_card())
    if player.get_value() > 21:
        outcome[0] = 'You went bust and lose.'
        outcome[1] = 'New deal?'
        score -= 1
        in_play = False

def stand():
    global outcome, in_play, score
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21 or dealer.get_value() < player.get_value():
            outcome[0] = 'You win.'
            outcome[1] = 'New deal?'
            score += 1
            in_play = False
        elif dealer.get_value() >= player.get_value():
            outcome[0] = 'You lose.'
            outcome[1] = 'New deal?'
            score -= 1
            in_play = False

# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Blackjack!', [100, 100], 50, 'Blue')
    canvas.draw_text('Dealer', [100, 180], 30, 'Black')
    canvas.draw_text('Player', [100, 380], 30, 'Black')
    canvas.draw_text(outcome[0], [240, 180], 24, 'Black')
    canvas.draw_text(outcome[1], [240, 380], 24, 'Black')
    canvas.draw_text('score: %d' % score, [480, 100], 24, 'Black')
    dealer.draw(canvas, [100, 200])
    player.draw(canvas, [100, 400])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
