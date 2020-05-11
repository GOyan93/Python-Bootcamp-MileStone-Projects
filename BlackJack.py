# Title: Black Jack Boot Camp Project
# Author: GOyan
# Description: A basic blackjack style game based on OOP in python.
# Python 3.6 

import random
import decimal
import sys

# Game Layout
    # COMPLETE Asks player for bet amount
    # COMPLETE Deals comp 2 cards (only 1 shows), player 2 cards
    # TODO Asks Player to hit or stand
        # After player stand, dealer rules come into play
    # COMPLETE Sums comp hand and sums player hand
        # If either over 21, bust and other wins
        # If both bust, comp wins
    # COMPLETE Compares comp sum and player sum
        # Greater or equal is player win
    # TODO
        #If bet > balance, first bet used for win deposit
        # Win does not add back to bank
        # Cards do not represent A, J, Q, K
        # Change order so player action between dealer first and second card
        # Introduction and Rules




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
        return handSum

    def hand_reset(self):
        self.hand = []


            
class Bank:
    def __init__(self, balance=int(1000)):
        self.balance = balance

    
    def __str__(self):
        return f'Account Balance: ${self.balance}'

    def deposit(self, winnings):
        self.balance += winnings
        print("The winnings of ${} have been deposited into your account. You have a total of ${}.".format(winnings, self.balance))   

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
            P1_bet()
        
    


def comparison(P1_card_sum, Comp_card_sum):
    if (P1_card_sum >= Comp_card_sum and P1_card_sum < 22) or (Comp_card_sum > 21 and P1_card_sum < 22):
        print('WIN! You have won the hand.')
        P1_bank.deposit(bet_amount * 2)
        # Win statement including sum values for both parties and deposit bet * 2 to bank
    elif (P1_card_sum < Comp_card_sum) and Comp_card_sum < 22:
        print('Lose. You have lost the hand.')
        
        # Loss statement including sum values for both parties and reset bet amount.
    elif P1_card_sum > 21:
        print('BUST. You have lost the hand.')
        
        # Bust statement including sum value for player and reset bet amount.
    

def P1_bet():
    print("How much would you like to bet?")
    amnt = int(input())
    return amnt

    
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

P1 = Player("P1")
P1_bank = Bank()
Comp = Player("Comp")
while game_on:
    deck = Deck()
    deck.shuffle()
    P1.hand_reset()
    Comp.hand_reset()
    
    print(P1_bank)
    bet_amount = P1_bet()
    P1_bank.bet(bet_amount)
    P1.draw(deck)
    P1.draw(deck)
    P1.showHand()
    #P1.showCardVal()
    #P1.cardSum()

    
    Comp.draw(deck)
    Comp.draw(deck)
    Comp.showHand()
    #Comp.showCardVal()
    #Comp.cardSum()

    comparison(P1.cardSum(), Comp.cardSum())
    
    if P1_bank.balance == 0:
        game_on = False
replay()
    
# Dealer rules:
    # When the player has played:
        # The second card is shown.
        # If dealer <= 16, the dealer must draw
        # If dealer >= 17, the dealer must stand
