# Title: Black Jack Boot Camp Project
# Author: GOyan
# Description: A basic blackjack style game based on OOP in python.
# Python 3.6 

import random


# Game Layout
    # Asks player for bet amount
    # Deals comp 2 cards (only 1 shows), player 2 cards
    # Asks Player to hit or stand
        # After player stand, dealer rules come into play
    # Sums comp hand and sums player hand
        # If either over 21, bust and other wins
        # If both bust, comp wins
    # Compares comp sum and player sum
        # Greater or equal is player win




# Create deck class
    # Full deck function
    # Must be randomly drawn
    # reset deck function
    # if sum is greater than 21, Ace = 1, else equals 11
    # Deck has 52 cards
    # Deck has 4 suits: Hearts, Clubs, Diamons, Spades
    # Cards, 2-10, J,Q,K (all worth 10), A (worth 1 or 11)

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print('{} of {}'.format(self.value, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Hearts", "Spades", "Clubs", "Diamonds"]:
              for value in range(1, 14):
                  self.cards.append(Card(suit, value))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()
            
deck = Deck()
deck.shuffle()

Greg = Player("Greg")
Greg.draw(deck)
Greg.draw(deck)
Greg.showHand()


# Create bank class
    # base amount to start bank
    # withdrawal function for betting
    # deposit function for wins
    # Alert function for when withdrawing more than bank amount
    # Alert function for when bank = 0

# Create win / loss check function

# Create bust check function


# Create a while loop to keep playing
    # if money  = 0, stop playing
    # if player inputs certain key, stops playing


    
# Dealer rules:
    # When the player has played:
        # The second card is shown.
        # If dealer <= 16, the dealer must draw
        # If dealer >= 17, the dealer must stand
