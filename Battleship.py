import random
import time

def build_board():                                                  #builds an 11 x 11 game board with a 10 x 10 playable space
    board = {}                                                      #returns a dictionary with Keys = letters A - J, each dict entry corresponds to one row of bame goard
    slots = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']      #board columns are numbered such that they are colated with array indicies for each dict entry
    swap = []
    for i in range(0, 11):
        swap.append(str(i))
    board[0] = swap
    swap = []
    for i in slots:
        for J in range(0, 9):
            swap.append("W")
        swap.append("W ")
        swap.insert(0, i)
        board[i] = swap
        swap = []
    return board

def show_board(player_board):                                       #shows the board in a visually appealing style that can be readily understood by the player
    for i in range(0,3):
        print(" ")
    for i in player_board:
        print(player_board[i])
    for i in range(0,3):
        print(" ")