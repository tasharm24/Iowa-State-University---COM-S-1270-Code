#Candy Land                         4/23/2025
#Natasha Mills
#Assignment 6

#This is an online version of the classic "Candy Land" boardgame! Called, Candy Realm, 
#this interactive game allows you to play with 2-4 people, picking colored cards and 
#advancing the board based on it. You can also shuffle the cards on the board if you want!



import random

players = 0
board = []
spaces = []

def main():
    global players
    print("------------------------------------------------")
    print("Welcome to Candy Realm!")
    print("This is a fun boardgame where you pick cards\nAnd advance along the board to the end!\nBut be careful! Danger awaits!")
    players = int(input("How many players will there be?"))
    print(f"You chose to play with {players} players!")
    print("Have fun!")
    print("------------------------------------------------")
    shuffleDeck()
    game()
    takeTurns(20)

def game():
    global positions
    global players
    global board
    global cols
    positions = {
        "1": [0, 4],
        "2": [1, 4],
        "3": [2, 4],
        "4": [3, 4]
    }
    if players == 2:
        cols = 20
        rows = players
        board = [[" " for _ in range(cols)] for _ in range(rows)]
        piece_position = [0, 3] 
        board[piece_position[0]][piece_position[1]] = "1"
        piece_position2 = [1, 3]
        board[piece_position2[0]][piece_position2[1]] = "2"
        print_board()
    elif players == 3:
        cols = 30
        rows = players
        board = [[" " for _ in range(cols)] for _ in range(rows)]
        piece_position = [0, 3]  
        board[piece_position[0]][piece_position[1]] = "1"
        piece_position2 = [1, 3]
        board[piece_position2[0]][piece_position2[1]] = "2"
        piece_position3 = [2, 3] 
        board[piece_position3[0]][piece_position3[1]] = "3"
        print_board()
    elif players == 4:
        cols = 40
        rows = players
        board = [[" " for _ in range(cols)] for _ in range(rows)]
        piece_position = [0, 3]  
        board[piece_position[0]][piece_position[1]] = "1"
        piece_position2 = [1, 3]
        board[piece_position2[0]][piece_position2[1]] = "2"
        piece_position3 = [2, 3] 
        board[piece_position3[0]][piece_position3[1]] = "3"
        piece_position4 = [3, 3] 
        board[piece_position4[0]][piece_position4[1]] = "4"
        print_board()
    
def print_board():
    global spaces
    for row in board:
        print(" " + " ".join(row) + " ")
    print("START:                                        :END")
    print("CARDS:", " ".join(spaces))

def shuffleDeck():
    global spaces
    spaces = ['R', 'Y', 'O', 'P', 'R', 'B', 'P', 'B', 'O', 'X', 'R', 'P', 'B', 'Y', 'O', 'B', 'P', 'X', 'R', 'B']
    random.shuffle(spaces)
    return spaces
spaces = shuffleDeck()

def moveSpot(player):
    for row_index in range(len(board)):
        for col_index in range(len(board[0])):
            if board[row_index][col_index] == player:
                board[row_index][col_index] = " "
                if col_index + 1 < len(board[0]):
                    board[row_index][col_index + 1] = player
                    takeTurns()
                else:
                    print("-------------------------------------------------------------------")
                    print(f"Player {player} has finished the game! You are the Realm Champion!")
                    main()

def takeTurns(turns):
    order = ["1", "2", "3", "4"][:players]
    for i in range(turns):
        current = order[i % players]
        print(f"It is player {current}'s turn!")
        yourTurn(current)
        print_board()

def yourTurn(player):
    choice = input(f"Player {player}, what would you like to do? [D]raw a card, [S]huffle the deck, [Q]uit?")
    if choice == "D":
        drawCard(player)
    if choice == "S":
        shuffleDeck()
    if choice == "Q":
        print("Goodbye!")
        exit()   

def drawCard(player):
    global colors
    global card
    global color
    global colorMap
    colors = {1: 'P', 2: 'R', 3: 'B', 4: 'O', 5: 'Y', 6: 'X', 7: '~'}
    card = random.randint(1,7)
    color = colors[card]
    colorMap = {
    'P': 'purple',
    'R': 'red',
    'B': 'blue',
    'O': 'orange',
    'Y': 'yellow', 
    'X': 'Gooey Gumdrops', 
    '~': 'Gumdrop Pass'}
    if card <= 5:
        print(color)
        movePlayer(player, color)
        print(f"Player {player} picked the {colorMap[color]} card!")
    elif card == 6:
        print(color)
        movePlayer(player, color)
        print(f"Player {player} picked the Gooooooey Gumdrops card!\n They lose a turn!!")
    elif color == 7:
        print(color)
        movePlayer(player, color)
        print(f"Player {player} picked the Gumdrop Passsss card!\n They advance further ahead!!")


def movePlayer(player, color):
    global colors
    global positions
    global colorMap
    global card
    color = colors[card]
    if card <= 5:
        for row_index in range(len(board)): # iterates over each row within the board
            for col_index in range(len(board[0])): #iterates over eahc column within a row
                print("1", col_index)
                if board[row_index][col_index] == player: #checks if the current cell has the player's piece
                    print("2", player)
                    print("3", row_index)
                    print("3.5", col_index)
                    for nextCol in range(col_index + 1, len(board[0])): #looks to the right to find a spot
                        print("4", nextCol)
                        print("5", col_index)
                        while spaces[nextCol] != color: #while the space to the right is not the right color,
                            print(spaces)
                            for nextCol in range(col_index + 1, len(board[0])): #keep looking to the right to find the right spot
                                print("nextCol", nextCol)
                                print("row", row_index)
                                print("col", col_index)
                                if spaces[nextCol] == color: #checks if the next space is the desired color
                                    positions[player] = [row_index, nextCol] #updates the player's position in the dictionary
                                    board[row_index][col_index] = " " #clears the original position of the player
                                    board[row_index][nextCol] = player #puts player in new position
                                    return
                                else:
                                    continue                             
    elif card == 6:
        color = card
        for row_index in range(len(board)):
            for col_index in range(len(board[0])):
                if board[row_index][col_index] == player:
                                for nextCol in range(col_index + 1, len(board[0])):
                                    if spaces[nextCol] == 6:
                                        board[row_index][col_index] = " "
                                        board[row_index][nextCol] = player
                                        positions[player] = [row_index, nextCol]
                                        return
                                    elif nextCol in range(col_index + 1, len(board[0])):
                                        if spaces[nextCol] == 6:
                                            board[row_index][col_index] = " "
                                            board[row_index][nextCol] = player
                                            positions[player] = [row_index, nextCol]
                                            return
    elif card == 7:
        color = card
        for row_index in range(len(board)):
            for col_index in range(len(board[0])):
                if board[row_index][col_index] == player:
                                for nextCol in range(col_index + 1, len(board[0])):
                                    if spaces[nextCol] == 7:
                                        board[row_index][col_index] = " "
                                        board[row_index][nextCol] = player
                                        positions[player] = [row_index, nextCol]
                                        return
                                    elif nextCol in range(col_index + 1, len(board[0])):
                                        if spaces[nextCol] == 7:
                                            board[row_index][col_index] = " "
                                            board[row_index][nextCol] = player
                                            positions[player] = [row_index, nextCol]
                                            return

    else:
                    print(f"Player {player} picked the {colorMap[color]} card!")
                    print("-------------------------------------------------------------------")
                    print(f"Player {player} has finished the game! You are the Realm Champion!")
                    main()
    return

if __name__ == "__main__":
    main()