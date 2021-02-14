import random
import time


class Piece:                                                                                                #Ship object to represent the game pieces
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

def build_fleet():                                                                                          #function to build an array that contains the player's ship objects
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

def show_things(player_board, player_fleet):                                                                #function to show the player's ship board and the player's fleet in a visually appealing fashion
    
    show_board(player_board)
    for i in range(3):
        print(" ")
    show_fleet(player_fleet)
    print(" ")

def pieces_remaining(player_fleet):                                                                         #function to return a list of the remaining unset ships
    x = []                                                                                                  #used to assist the computer player in setting its fleet
    for i in range(1, 6):
        if player_fleet[i].is_set == "N":
            x.append(i)
        else:
            continue
    return x

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

def set_piece(ship, target, direction, player_board, player_fleet):                                         #function to set a player's selected ship in a validated position on the player's fleet board
                                                                                                            #contains 4 functions relative to each cardinal direction
    def east():                                                                                             #sets the selected ship.is_set to "Y"
        x = player_fleet[ship].size - 1                                                                     #utilizes a dictionary to run the appropriate function based on the players input
        y = 1                                                                                               #for each ship segment, inserts the quadrant it occupies
        z = player_fleet[ship].name[0]                                                                      #for each quadrant occupied by a ship segment, inserts the first letter of the ship into the fleet board quadrant
        swap = target
        while x != 0:
            for i in range(x):
                swap = swap[0] + str(int(1 + int(swap[1:])))
                player_board[target[0]][y + int(target[1:])] = z
                player_fleet[ship].positions[0 + y] = swap
                x -= 1
                y += 1

    def west():
        x = player_fleet[ship].size - 1
        y = -1
        z = player_fleet[ship].name[0]
        swap = target
        while x != 0:
            for i in range(x):
                swap = swap[0] + str(int(int(swap[1:]) - 1))
                player_board[target[0]][y + int(target[1:])] = z
                player_fleet[ship].positions[abs(y)] = swap
                x -= 1
                y -= 1
                

    def north():
        x = player_fleet[ship].size - 1
        y = -1
        z = player_fleet[ship].name[0]
        swap = target
        while x != 0:
            for i in range(x):
                swap = chr(ord(target[0]) + y) + swap[1:]
                player_board[chr(ord(target[0]) + y)][int(target[1:])] = z
                player_fleet[ship].positions[abs(y)] = swap
                x -= 1
                y -= 1
                
    def south():
        x = player_fleet[ship].size - 1
        y = 0
        z = player_fleet[ship].name[0]
        swap = target
        while x != 0:
            for i in range(x):
                swap = chr(ord(target[0]) + 1 + y) + swap[1:]
                player_board[chr(ord(target[0]) + 1 + y)][int(target[1:])] = z
                player_fleet[ship].positions[1 + y] = swap
                x -= 1
                y += 1
            
                
    switcher = {"E": east, "W": west, "N": north, "S": south}

    func = switcher.get(direction, lambda: 1/0)

    
    player_board[target[0]][int(target[1:])] = player_fleet[ship].name[0]
    player_fleet[ship].positions[0] = target
    player_fleet[ship].is_set = "Y"
    func()

def set_fleet(player_board, player_fleet):                                                                  #primary function to set a player's fleet
                                                                                                            #utilizes the is_set function to stay active until all pieces in a player's fleet are set
    show_things(player_board, player_fleet)                                                                 
                                                                                                            
    while is_set(player_fleet):                                                                             #queries player for the desired ship to set, and checks to see if that piece is set
        try:                                                                                                #if input is invalid or ship has been set, advises player and stays in loop until a valid ship has been selected
            ship = int(input("Please select the ship you would like to place: "))
            if ship not in range(1,6):
                raise ValueError
            elif player_fleet[ship].is_set == "Y":
                print(" ")
                print("You have already set this ship")
                raise ValueError
            else:
                break
        except ValueError:
            print(" ")
            print("Please input the corresponding number of the ship you would like to set.")
            print(" ")
            show_things(player_board, player_fleet)
    
    while is_set(player_fleet):                                                                             #queries player for an initial quadrant to set the selected ship on the player's ship board
        try:                                                                                                #if input is invalid, advises player and stays in loop until a valid quadrant has been selected
            print(" ")                                                                                      #if input is valid, utilizes check_target to determine if the quadrant is occupied
            target = input("Which quadrant would you like to set it in? ").upper()                          #if the quadrant is occupied stays in loop until an unoccupied quadrant has been selected
            if ord(target[0]) in range(ord("A"), ord("K")):
                if int(target[1:]) in range(1, 11):
                    if check_target(target, player_board) == True:
                        break
                    else:
                        raise ValueError("You have selected an occupied quadrant. Please make another choice.")
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print(" ")
            print("Please enter the letter of the row and the number of the column for the quadrant you would like to set your ship.")
            print(" ")
            show_things(player_board, player_fleet)

    while is_set(player_fleet):                                                                             #queries the player for the direction they want the ship to be placed in
        try:                                                                                                #if input is invalid, advises player and stays in loop until a valid direction has been selected
            cardinals = ["N", "S", "E", "W"]                                                                #if input is valid, utilizes check_direction to determine if the direction is unobstructed
            print(" ")                                                                                      #if the direction is obstructed stays in loop until a valid direction has been selected
            print(cardinals)
            print(" ")
            direction = input("Please select what direction you would like the ship to face: ").upper()
            if direction in cardinals:
                if check_direction(ship, target, direction, player_board, player_fleet) == True:
                    break
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print(" ")
            print("There was a problem with the direction you chose and you must make a different selection.")
            print(" ")
            print("Please select the first letter of one of the four cardinal directions as listed.")
            print(" ")
            show_things(player_board, player_fleet)
    
    set_piece(ship, target, direction, player_board, player_fleet)                                          #if the selections pass all previous checks, utilizes set_piece to associate the selected ship's position on the player's fleet board
    while is_set(player_fleet) != False:                                                                    #this function calls itself recursively until all ships in a player's fleet have been set
        set_fleet(player_board, player_fleet)

x = build_board()
show_board(x)