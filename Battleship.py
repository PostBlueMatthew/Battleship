import random
import time


class Piece:                                                                                                #creates Piece object to represent the various ships in the game with self-contained build function
    def __init__(self, name, size):                                                                         
        self.size = size
        self.name = name
        self.is_set = "N"
        self.is_sunk = "N"
        self.direction = ""
        self.positions =[]
        
    def build_piece(self):
        for i in range(0, self.size):
            self.positions.append(self.name[0])

def build_board():                                                                                          #builds an 11 x 11 game board with a 10 x 10 playable space
    board = {}                                                                                              #returns a dictionary with Keys = letters A - J, each dict entry corresponds to one row of game board
    slots = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']                                              #board columns are numbered such that they are colated with array indicies for each dict entry
    swap = []
    for i in range(0, 11):
        swap.append(str(i))
    swap[0] = " "
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

def show_board(player_board):                                                                               #shows the board in a visually appealing style that can be readily understood by the player
    for i in range(0,3):
        print(" ")
    for i in player_board:
        print(player_board[i])
    for i in range(0,3):
        print(" ")

def build_fleet():                                                                                          #builds an array to contain the player's fleet objects
    ships = [["Carrier", 5], ["Battleship", 4], ["Destroyer", 3], ["Submarine", 3], ["Patrol Boat", 2]]     #contains a list of player piece names and sizes
    temp = [0]                                                                                              #builds each piece as per list and appends it to a fleet array
                                                                                                            #Pieces are added to the array such that they colate to the 1-5 indicies
    for i in range(0, len(ships)):
        x = Piece(ships[i][0], ships[i][1])
        x.build_piece()
        temp.append(x)
        
    return temp

x = build_board()
show_board(x)