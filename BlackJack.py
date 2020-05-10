# Title: Black Jack Boot Camp Project
# Author: GOyan
# Description: A basic blackjack style game based on OOP in python.
# Python 3.6 

import random
import decimal
import sys

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
    # Shuffled every turn 
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

    def showVal(self):
        print('{}'.format(self.value))

    def valueReturn(self):
        return self.value
        
    
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

    def showVal(self):
        for c in self.cards:
            c.showVal()

    def valueReturn(self):
        for c in self.cards:
            c.valueReturn()

            
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

    def sumHand(self):
        for i in range(len(self.hand)):
            self.hand[i]

    def showCardVal(self):
        for card in self.hand:
            card.showVal()

    def cardSum(self):
        val1 = int(self.hand[0].valueReturn())
        val2 = int(self.hand[1].valueReturn())
        handSum = (val1 + val2)
        print(handSum)

            
class Bank:
    def __init__(self, balance = 1000.00):
        self.balance = balance

    
    def __str__(self):
        return f'Account Balance: ${self.balance}'
        
    def bet(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print("You have bet ${}. There is ${} remaining in your account.".format(amount, self.balance))
        elif amount == self.balance:
            self.balance -= amount
            print("You have bet ${}.".format(amount))
            print("!!!ALERT!!!\nYou have ZERO remaining funds!")
        else:
            print("You do not have enough funds.")

    def deposit(self, winnings):
        self.balance += winnings
        print("The winnings of ${} have been deposited into your account. You have a total of ${}.".format(winnings, self.balance))


            
# Replay function for when bank = 0.  
def replay():
    player_input = input('Would you like to reset bank and play again? (Yes or No): ')
    if player_input[0].upper() == 'Y':
        game_on = True
        
    else:
        game_on = False
        print('Thank you for playing!')
        sys.exit()
# Create win / loss check function

# Create bust check function


# Create a while loop to keep playing
    # if money  = 0, stop playing
    # if player inputs certain key, stops playing

game_on = True

while game_on:
    deck = Deck()
    deck.shuffle()

    P1 = Player("P1")
    P1.draw(deck)
    P1.draw(deck)
    #P1.showHand()
    P1.showCardVal()
    P1.cardSum()

    Comp = Player("Comp")
    Comp.draw(deck)
    Comp.draw(deck)
    #Comp.showHand()
    Comp.showCardVal()
    Comp.cardSum()
    replay()
    
# Dealer rules:
    # When the player has played:
        # The second card is shown.
        # If dealer <= 16, the dealer must draw
        # If dealer >= 17, the dealer must stand
