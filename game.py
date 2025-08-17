from shutil import move
import pandas as pandas
import numpy as np

board = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
print(board)
for i in range(10):
    move_x = int(input("enter row"))
    move_y = int(input("enter column"))

    board[move_x][move_y] = 3

    print(board)

    move_x1 = int(input("enter row"))
    move_y1 = int(input("enter column"))

    if move_x1 == move_x and move_y1 == move_y:
        board[move_x][move_y] = 0
        board[move_x-1][move_y] = 1
        board[move_x][move_y-1] = 1
        board[move_x+1][move_y] = 1
        board[move_x][move_y+1] = 1
        print(board)
    else:
        board[move_x1][move_y1] = 3
        print(board)



