#TicTacToe Game
#python 3.6.9
#Author:GOyan

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}



def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'] + '\n' +
          '-' + '+' + '-' + '+' + '-' + '\n' +
          board['4'] + '|' + board['5'] + '|' + board['6'] + '\n' +
          '-' + '+' + '-' + '+' + '-' + '\n' +
          board['1'] + '|' + board['2'] + '|' + board['3'])

def playerONEchoice(playerONEinput):
    theBoard[playerONEinput] = player1
    printBoard(theBoard)
    
def playerTWOchoice(playerTWOinput):
    theBoard[playerTWOinput] = player2
    printBoard(theBoard)

def win():
    print('Congratulations! You won!')
    
def winConditions():
    # Horizontal Wins
    if theBoard[7] == 'X' and theBoard[8] == 'X' and theBoard[9] == 'X':
        return True
        win()
    elif theBoard[4] == 'X' and theBoard[5] == 'X' and theBoard[6] == 'X':
        return True
        win()
    elif theBoard[1] == 'X' and theBoard[2] == 'X' and theBoard[3] == 'X':
        return True
        win()
    elif theBoard[7] == 'O' and theBoard[8] == 'O' and theBoard[9] == 'O':
        return True
        win()
    elif theBoard[4] == 'O' and theBoard[5] == 'O' and theBoard[6] == 'O':
        return True
        win()
    elif theBoard[1] == 'O' and theBoard[2] == 'O' and theBoard[3] == 'O':
        return True
        win()
        
    # Vertical Wins
    elif theBoard[7] == 'X' and theBoard[4] == 'X' and theBoard[1] == 'X':
        return True
        win()
    elif theBoard[8] == 'X' and theBoard[5] == 'X' and theBoard[2] == 'X':
        return True
        win()
    elif theBoard[9] == 'X' and theBoard[6] == 'X' and theBoard[3] == 'X':
        return True
        win()
    elif theBoard[7] == 'O' and theBoard[4] == 'O' and theBoard[1] == 'O':
        return True
        win()
    elif theBoard[8] == 'O' and theBoard[5] == 'O' and theBoard[2] == 'O':
        return True
        win()
    elif theBoard[9] == 'O' and theBoard[6] == 'O' and theBoard[3] == 'O':
        return True
        win()

    #Diagonal Wins
    elif theBoard[7] == 'X' and theBoard[5] == 'X' and theBoard[3] == 'X':
        return True
        win()
    elif theBoard[9] == 'X' and theBoard[5] == 'X' and theBoard[1] == 'X':
        return True
        win()
    elif theBoard[7] == 'O' and theBoard[5] == 'O' and theBoard[3] == 'O':
        return True
        win()
    elif theBoard[9] == 'O' and theBoard[5] == 'O' and theBoard[1] == 'O':
        return True
        win()
    return False


        
#TODO Add introduction and rules.
printBoard(theBoard)

#Player selection.
print('Player 1: Please select X or O.') 
player1 = input()

if player1 = 'X':
    player2 = 'O'
    
elif player1 = 'O':
    player2 = 'X'
    print('Player 1: X, Player 2: O')

# Main game loop.
while True:
    if winConditions() = True:
        break
    
    for i in range(9):
        print('PLAYER 1: Choose your position.')
        playerONEInput = input()
        playerONEchoice(playerONEInput)

        print('PLAYER 2: Choose your position.')
        playerTWOInput = input()
        playerTWOchoice(playerTWOInput)
