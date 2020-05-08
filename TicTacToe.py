#TicTacToe Game
#python 3.6.9
#Author:GOyan

#TODO Add working replay function. Polish board up. Add game/win counter.


import sys

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

def exampleBoard():
    print('7' + '|' + '8' + '|' + '9' + '\n' +
          '-' + '+' + '-' + '+' + '-' + '\n' +
          '4' + '|' + '5' + '|' + '6' + '\n' +
          '-' + '+' + '-' + '+' + '-' + '\n' +
          '1' + '|' + '2' + '|' + '3')

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'] + '\n' +
          '-' + '+' + '-' + '+' + '-' + '\n' +
          board['4'] + '|' + board['5'] + '|' + board['6'] + '\n' +
          '-' + '+' + '-' + '+' + '-' + '\n' +
          board['1'] + '|' + board['2'] + '|' + board['3'])

def playerONEchoice(playerONEinput):
    theBoard[playerONEinput.upper()] = player1
    printBoard(theBoard)
    
def playerTWOchoice(playerTWOinput):
    theBoard[playerTWOinput.upper()] = player2
    printBoard(theBoard)

def win():
    print('Congratulations! You won!')
    
def winConditions():
    # Horizontal Wins
    if theBoard['7'] == 'X' and theBoard['8'] == 'X' and theBoard['9'] == 'X':
        return True
    elif theBoard['4'] == 'X' and theBoard['5'] == 'X' and theBoard['6'] == 'X':
        return True
    elif theBoard['1'] == 'X' and theBoard['2'] == 'X' and theBoard['3'] == 'X':
        return True
    elif theBoard['7'] == 'O' and theBoard['8'] == 'O' and theBoard['9'] == 'O':
        return True
    elif theBoard['4'] == 'O' and theBoard['5'] == 'O' and theBoard['6'] == 'O':
        return True
    elif theBoard['1'] == 'O' and theBoard['2'] == 'O' and theBoard['3'] == 'O':
        return True
        
    # Vertical Wins
    elif theBoard['7'] == 'X' and theBoard['4'] == 'X' and theBoard['1'] == 'X':
        return True
    elif theBoard['8'] == 'X' and theBoard['5'] == 'X' and theBoard['2'] == 'X':
        return True
    elif theBoard['9'] == 'X' and theBoard['6'] == 'X' and theBoard['3'] == 'X':
        return True
    elif theBoard['7'] == 'O' and theBoard['4'] == 'O' and theBoard['1'] == 'O':
        return True
    elif theBoard['8'] == 'O' and theBoard['5'] == 'O' and theBoard['2'] == 'O':
        return True
    elif theBoard['9'] == 'O' and theBoard['6'] == 'O' and theBoard['3'] == 'O':
        return True

    #Diagonal Wins
    elif theBoard['7'] == 'X' and theBoard['5'] == 'X' and theBoard['3'] == 'X':
        return True
    elif theBoard['9'] == 'X' and theBoard['5'] == 'X' and theBoard['1'] == 'X':
        return True
    elif theBoard['7'] == 'O' and theBoard['5'] == 'O' and theBoard['3'] == 'O':
        return True
    elif theBoard['9'] == 'O' and theBoard['5'] == 'O' and theBoard['1'] == 'O':
        return True
    return False

# Main game loop. Loop does not stop after win!
def mainGame():
    
        print('PLAYER 1: Choose your position.')
        playerONEInput = input()
        while int(playerONEInput) > 9 or int(playerONEInput) < 1:
            print("Please select a position between 1 and 9.")
            playerONEInput = input()
        else:
            playerONEchoice(playerONEInput.upper())
        
        print('PLAYER 2: Choose your position.')
        playerTWOInput = input()
        while int(playerTWOInput) > 9 or int(playerTWOInput) < 1:
            print("Please select a position between 1 and 9.")
            playerTWOInput = input()
        else:
            playerTWOchoice(playerTWOInput.upper())
        
def replay():
    print('Would you like to play again? (Y/N)')
    yesNo = input()
    if str(yesNo) == 'Y' or 'y': 
        theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}
        winConditions = False
        while winConditions() == False:
            mainGame()
            if winConditions() == True:
                win()
    else:
        sys.exit()
        
#TODO Add introduction and rules.
print("""Welcome to TIC TAC TOE!

THE RULES

1. 2 Players. 1st player goes first and chooses X or O.
2. Each turn a player will choose a spot on the board to place their piece.\n""")
exampleBoard()
print("\n3. The first person to get three pieces in a row (horizontal, vertical or diagonal wins!\n")

#Player selection.
print('Player 1: Please select X or O.')
player1 = input()
printBoard(theBoard)

if player1.upper() == 'X':
    player2 = 'O'
    print('Player 1: X, Player 2: O')
elif player1.upper() == 'O':
    player2 = 'X'
    print('Player 1: O, Player 2: X')
    
while winConditions() == False:
    mainGame()
    if winConditions() == True:
        win()
        #replay()
    else:
        continue

