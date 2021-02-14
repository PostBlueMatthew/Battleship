import random
import time


class Piece:                                                                                                #Ship object to represent the various ships in the game with self-contained build function
    def __init__(self, name, size):                                                                         
        self.size = size
        self.name = name
        self.is_set = "N"
        self.is_sunk = "N"
        self.direction = ""
        self.positions =[]
        
    def build_piece(self):                                                                                  #build command makes a string array of the first initial of the ship type, self.size long
        for i in range(0, self.size):
            self.positions.append(self.name[0])

def build_board():                                                                                          #function that builds an 11 x 11 game board with a 10 x 10 playable space
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

def show_board(player_board):                                                                               #function to show a game board in a visually appealing style that can be readily understood by the player
    for i in range(0,3):
        print(" ")
    for i in player_board:
        print(player_board[i])
    for i in range(0,3):
        print(" ")

def build_fleet():                                                                                          #function to build an array that contains the player's fleet objects
    ships = [["Carrier", 5], ["Battleship", 4], ["Destroyer", 3], ["Submarine", 3], ["Patrol Boat", 2]]     #contains a list of player piece names and sizes
    temp = [0]                                                                                              #builds each piece as per list and appends it to a fleet array
                                                                                                            #Pieces are added to the array such that they colate to the 1-5 indicies
    for i in range(0, len(ships)):
        x = Piece(ships[i][0], ships[i][1])
        x.build_piece()
        temp.append(x)
        
    return temp

def show_fleet(fleet):                                                                                      #function that takes one fleet array and displays all segments of each fleet piece
                                                                                                            #each segment lists what quadrant it occupies on the player's board
                                                                                                            #if the piece segment contains the first letter of its ship type the piece is unset
    for i in range(1, len(fleet)):
        print(i, end=" - ")
        print(fleet[i].positions)

def is_set(player_fleet):                                                                                   #function to check each piece.is_set attribute in the fleet array and returns true/false if fleet is set/not set
        x = 0
        for i in range(1, 6):
            if player_fleet[i].is_set == "N":
                x += 1
            else:
                continue
        return x != 0

def check_target(target, player_board):                                                                     #function to check if a quadrant in a player's board is unoccupied
                                                                                                            #checks player.s input to ensure it is valid - raises a ValueError if it is not
    check_row = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']                                          #retuns True if unoccupied, False otherwise
    check_column = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    if target[0] in check_row:
        if int(target[1:]) in check_column:
            if player_board[target[0]][int(target[1:])] == "W":
                return True
            elif player_board[target[0]][int(target[1:])] == "W ":
                return True
            else:
                return False
        else:
            raise ValueError
    else:
        raise ValueError

def check_direction(ship, target, direction, player_board, player_fleet):                                   #function to check if a selected direction contains the required amount of unoccupied quadrants on a player's board
                                                                                                            #the player inputs an initial quadrant and a direction to specify where their ship piece is to be placed
    def east():                                                                                             #initial quadrant is checked first using check_target and if it is valid check_direction is initiated
        if player_fleet[ship].size <= len(player_board[target[0]][int(target[1:]):]):                       #if a target direction satisfies size requirements the function returns True
            x = player_fleet[ship].size - 1                                                                 #if a target direction contains occupied quadrants or there are insufficient quadrants to fit the selected piece the function raises a ValueError to the console
            y = 1                                                                                           #contains 4 functions that each check a single cardinal direction
            while x != 0:                                                                                   #utilizes a dictionary to return the appropriate function based on the players input
                for i in range(x):
                    if player_board[target[0]][y + int(target[1:])] == "W" or player_board[target[0]][y + int(target[1:])] == "W ":         
                        x -= 1                                                                                                              
                        y += 1                                                                                                              
                    else:
                        return False
                        break
            return True

        else:
            raise ValueError("Directional Error Occurred - E")

    def west():
        if player_fleet[ship].size <= len(player_board[target[0]][1:1 + int(target[1:])]):
            x = player_fleet[ship].size - 1
            y = -1
            while x != 0:
                for i in range(x):
                    if player_board[target[0]][y + int(target[1:])] == "W" or player_board[target[0]][y + int(target[1:])] == "W ":
                        x -= 1
                        y -= 1
                    else:
                        return False
                        break
            return True
        else:
            raise ValueError("Directional Error Occurred - W")

    def north():
        if (ord(target[0]) - ord("A") + 1) >= player_fleet[ship].size:
            x = player_fleet[ship].size - 1
            y = -1
            while x != 0:
                for i in range(x):
                    if player_board[chr(ord(target[0]) + y)][int(target[1:])] == "W" or player_board[chr(ord(target[0]) + y)][int(target[1:])] == "W ":
                        x -= 1
                        y -= 1
                    else:
                        return False
                        break
            return True
        else:
            raise ValueError("Directional Error Occurred - N")

    def south():
        if (ord("J") - ord(target[0]) + 1) >= player_fleet[ship].size:
            x = player_fleet[ship].size - 1
            y = 0
            while x != 0: 
                for i in range(x):
                    if player_board[chr(ord(target[0]) + 1 + y)][int(target[1:])] == "W" or player_board[chr(ord(target[0]) + 1 + y)][int(target[1:])] == "W ":
                        x -= 1
                        y += 1
                    else:
                        return False
                        break
            return True
        else:
            raise ValueError("Directional Error Occurred - S")

    switcher = {"E": east, "W": west, "N": north, "S": south}

    func = switcher.get(direction, lambda: 1/0)
    return func()


x = build_board()
show_board(x)