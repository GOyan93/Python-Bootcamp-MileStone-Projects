# Title: Black Jack Boot Camp Project
# Author: GOyan
# Description: A basic blackjack style game based on OOP in python.
# Python 3.6 

import random
import decimal
import sys
import time
# Game Layout
    # COMPLETE Asks player for bet amount
    # COMPLETE Deals comp 2 cards (only 1 shows), player 2 cards
    # COMPLETE 
        # After player stand, dealer rules come into play
    # COMPLETE Sums comp hand and sums player hand
        # If either over 21, bust and other wins
        # If both bust, comp wins
    # COMPLETE Compares comp sum and player sum
        # Greater or equal is player win
    # TODO
        # If bet > balance, first bet used for win deposit.
            # If loss, bank resets to 1000.
        # Cards do not represent A, J, Q, K
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
        print("{}'s cards:\n".format(self.name))
        for card in self.hand:
            card.show()
        print("--------------")
        
    def sumHand(self):
        for i in range(len(self.hand)):
            self.hand[i]
            

    def showCardVal(self):
        for card in self.hand:
            card.showVal()

    def cardSum(self):
        vals = []
        
        for i in range(len(self.hand)):
            vals.append(self.hand[i].valueReturn())
            
        handSum = sum(vals)
        print("{}'s card sum:\n".format(self.name))
        print(str(handSum) + "\n--------------")
        return handSum

    def hand_reset(self):
        self.hand = []

    def action(self):
        hit = True
        while hit == True:
            print("Would you like to hit of stand?")
            action = input().lower()
            if action == 'hit':
                hit = True
                self.draw(deck)
                self.showHand()
            if self.cardSum() > 21 or action != 'hit':
                hit = False
                pass

            
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

    
  
def replay():
    player_input = input('Would you like to reset bank and play again? (Yes or No): ')
    if player_input[0].upper() == 'Y':
        P1_bank.deposit(1000)
        game_on = True
        
    else:
        game_on = False
        print('Thank you for playing!')
        sys.exit()







game_on = True

P1 = Player("P1")
P1_bank = Bank()
Dealer = Player("Dealer")
while game_on:
    deck = Deck()
    deck.shuffle() 
    P1.hand_reset() 
    Dealer.hand_reset()     # Shuffles deck for each round and resets hands
    
    print(P1_bank)
    bet_amount = P1_bet()   # Asks player for bet before cards are dealt
    P1_bank.bet(bet_amount)
    P1.draw(deck)
    P1.draw(deck)           
    Dealer.draw(deck)       # Deals 2 cards to player, 1 to Dealer
    P1.showHand()
    Dealer.showHand()
    if P1.cardSum() < 22:   # If player has not bust, asks for player action
        P1.action()
    #P1.showCardVal()
    #P1.cardSum()

    
    while Dealer.cardSum() <= 16 and P1.cardSum() < 22:   # After player stands, dealer draws depending on sum of cards.
        Dealer.draw(deck)
        Dealer.showHand()
        time.sleep(1)
    P1.showHand()
    Dealer.showHand()
    
    #Comp.showCardVal()
    #Comp.cardSum()

    comparison(P1.cardSum(), Dealer.cardSum())
    
    if P1_bank.balance == 0:
        replay()
    
# Dealer rules:
    # When the player has played:
        # The second card is shown.
        # If dealer <= 16, the dealer must draw
        # If dealer >= 17, the dealer must stand
