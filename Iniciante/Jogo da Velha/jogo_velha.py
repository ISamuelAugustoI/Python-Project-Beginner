"""
Author: Samuel Augusto
Date: 22/12/2024
Description: Jogo que simula um jogo da velha
"""
grid = [[0,0,0],[0,0,0],[0,0,0]]
won = False
player = 0
def board(grid):
    for i in range(0,3):
        for j in range(0,3):
            if grid[i][j] == 0:
                print(" _ ", end=' ')
            elif grid[i][j] == 1:
                print(" X ", end=' ')
            elif grid[i][j] == -1:
                print(" O ", end=' ')
        print()
def is_full(grid):
    for row in grid:
        if 0 in row:
            return 0
    return 1
def victory():
    for i in range(3):
        sum = grid[0][0]
    for i in range(3):
        sum = grid[i][0]+grid[i][1]+grid[i][2]
        if(sum==3 or sum ==-3):
            return 1
    for i in range(3):
        sum = grid[0][i]+grid[1][i]+grid[2][i]
        if(sum==3 or sum==-3):
            return 1
    diagonal1 = grid[0][0]+grid[1][1]+grid[2][2]
    diagonal2 = grid[0][2]+grid[1][1]+grid[2][0]
    if(diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3):
        return 1
    return 0
print(f'================================')
print(f'Welcome to the Tic Tac Toe Game:') 
while(won==False):
    print(f'\nPlayer {player%2 + 1} turn:')
    board(grid)
    cols = int(input('Enter the cols[1-3]: '))
    lins = int(input('Enter the lins[1-3]: '))
    if(grid[lins-1][cols-1]==0):
        if((player%2+1)==1):
            grid[lins-1][cols-1]=1
        else:
            grid[lins-1][cols-1]=-1
    else:
        print('Any player has already filled it out')
        player-=1
    if(victory()):
        print(f'Player {player%2+1} has victory after {player+1} rounds')
        board(grid)
        won = True
        break
    if(is_full(grid)):
        print("It's a draw! No more moves possible.")
        board(grid)
        break
    player+=1