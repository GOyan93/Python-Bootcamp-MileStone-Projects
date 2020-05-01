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

printBoard(theBoard)

player1 = X


player2 = O



def playerONEchoice(playerONEinput)
    playerONEInput = input()
    theBoard[playerONEinput] = player1
    printBoard(theBoard)
    
def playerTWOchoice(playerTWOinput)
    playerTWOInput = input()
    theBoard[playerTWOinput] = player2
    printBoard(theBoard)
