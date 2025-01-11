"""
Author: Samuel Augusto
Date: 23/12/2024
Description: Código que simula um jogo de batalha naval
"""
# Import and Create Variables:
import random
ships = {'Destroyer':[2,2],
        'Submarine': [2,3],
        'Cruiser':   [2,3],
        'Battleship':[1,4],
        'Carrier':   [1,5]
}
# Create and Display Board:
def create_board(size=10):
    return [['-' for _ in range(size)] for _ in range(size)]
def display_board(board):
    print("\n-------- Board --------")
    letters = "ABCDEFGHIJ"
    print("   " + " ".join(letters[:len(board)]))
    for i,j in enumerate(board):
        print(f"{i + 1:2} " + " ".join(j))
    print()
# Create and positioning the ships:
def check_position(board,lins,cols,size,direction):
    for i in range(size):
        if(direction=='horizontal'):
            if(cols+i>=len(board) or board[lins][cols+i] != '-'):
                return False
        elif(direction=='vertical'):
            if(lins+i>=len(board) or board[lins+i][cols] != '-'):
                return False
    return True
def position_ships(board,lins,cols,size,direction,symbol,ship_positions):
    positions = []
    for i in range(size):
        if(direction=='horizontal'):
            board[lins][cols+i] = symbol
            positions.append((lins,cols+i))
        elif(direction=='vertical'):
            board[lins+i][cols] = symbol
            positions.append((lins+i,cols))
    ship_positions[symbol] = positions
def position_all_ships(board,ships):
    ship_positions = {}
    for ship,(quantity, size) in ships.items():
        for _ in range(quantity):
            placed = False
            while not placed:
                row = random.randint(0, len(board) - 1)
                col = random.randint(0, len(board) - 1)
                direction = random.choice(['horizontal', 'vertical'])
                if check_position(board, row, col, size, direction):
                    position_ships(board, row, col, size, direction, ship[0], ship_positions)
                    placed = True
    return ship_positions
# Record Shot Ships:
def record_shot(board,visible_board,row,col,ship_positions):
    if board[row][col] != '-':
        ship_symbol = board[row][col]
        visible_board[row][col] = 'X'
        print(f"Nice! You hit a ship!")
        if (row, col) in ship_positions[ship_symbol]:
            ship_positions[ship_symbol].remove((row, col))
        if not ship_positions[ship_symbol]:
            print(f"You sank the {ship_symbol}!")
    else:
        visible_board[row][col] = 'O'
        print(f"Miss! That was just water.")
# Check Victory:
def check_victory(ship_positions):
    return all(not positions for positions in ship_positions.values())
# Game:
board = create_board(10)
visible_board = create_board(10)
ship_positions = position_all_ships(board,ships)
print(f'============================')
print(f'Welcome to the Naval Battle:')
display_board(visible_board)
display_board(board)
while True:
    cols_input = input('Enter the cols: ').upper()
    cols = ord(cols_input) - ord('A')
    lins = int(input('Enter the lins: '))-1
    if(0<=lins<10 and 0<=cols<10):
        record_shot(board,visible_board,lins,cols,ship_positions)
        display_board(visible_board)
        if(check_victory(ship_positions)):
            print("Congratulations! You've sunk all the ships!")
            break
    else:
        print("Invalid coordinates. Please try again.")