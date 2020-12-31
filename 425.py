# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:45:13 2020

@author: Alfredo
"""

# Daily Coding Problem #425

# Problem:
# You are presented with an 8 by 8 matrix representing the positions of pieces
# on a chess board. The only pieces on the board are the black king and various
# white pieces. Given this matrix, determine whether the king is in check.



# diagonally check for queen, bishops, and pawns
def bishops(board, y, x):
    
    # up, right
    i = y - 1
    j = x + 1
    while i >= 0 and j < 8:
        if board[i][j] == 'Q' or board[i][j] == 'B':
            return True
        
        if board[i][j] != '.':
            break
        i -= 1
        j += 1
            
    #up, left
    i = y - 1
    j = x - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q' or board[i][j] == 'B':
            return True
        
        if board[i][j] != '.':
            break
        i -= 1
        j -= 1
        
    #down, right
    i = y + 1
    j = x + 1
    
    if board[i][j] == 'P':
        return True
    
    while i < 8 and j < 8:
        if board[i][j] == 'Q' or board[i][j] == 'B':
            return True
        
        if board[i][j] != '.':
            break
        i += 1
        j += 1
        
    #down, left
    i = y + 1
    j = x - 1
    
    if board[i][j] == 'P':
        return True
    
    while i < 8 and j >= 0:
        if board[i][j] == 'Q' or board[i][j] == 'B':
            return True
        
        if board[i][j] != '.':
            break
        i += 1
        j -= 1 
    
    return False


# vertically and horizontally check for queen and rooks
def rooks(board, y, x):
    
    # up
    for i in range(y-1, -1, -1):
        if board[i][x] == 'Q' or board[i][x] == 'R':
            return True
        
        if board[i][x] != '.':
            break
        
    # down
    for i in range(y+1, 8):
        if board[i][x] == 'Q' or board[i][x] == 'R':
            return True
        
        if board[i][x] != '.':
            break
    
    # left
    for j in range(x-1, -1, -1):
        if board[y][j] == 'Q' or board[y][j] == 'R':
            return True
        
        if board[y][j] != '.':
            break
    
    # right
    for i in range(x+1, 8):
        if board[y][j] == 'Q' or board[y][j] == 'R':
            return True
        
        if board[y][j] != '.':
            break
    
    return False


# check for knights
def knights(board, y, x):
    if y > 0:
        if x > 1:
            if board[y-1][x-2] == 'N':
                return True
        if x < 6:
            if board[y-1][x+2] == 'N':
                return True
    if y > 1:
        if x > 0:
            if board[y-2][x-1] == 'N':
                return True
        if x < 7:
            if board[y-2][x+1] == 'N':
                return True
            
    if y < 7:
        if x > 1:
            if board[y+1][x-2] == 'N':
                return True
        if x < 6:
            if board[y+1][x+2] == 'N':
                return True
    
    if y < 6:
        if x > 0:
            if board[y+2][x-1] == 'N':
                return True
        if x < 7:
            if board[y+2][x+1] == 'N':
                return True
        
    return False


# we find the position of the king and from there, we scan the board
def isCheck(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'K':
                return bishops(board, i, j) or rooks(board, i, j) or knights(board, i, j)

# -----------------------------------------------------------------------------
# Testing

b = [
     '...K....',
     '........',
     '.B......',
     '......P.',
     '.......R',
     '..N.....',
     '........',
     '.....Q..'
]
isCheck(b)          # True

b = [
     '...K....',
     '....P...',
     '.B......',
     '......P.',
     '.......R',
     '..N.....',
     '........',
     '.....Q..'
]
isCheck(b)          # True


b = [
     '...K....',
     '..RP....',
     '.B.R....',
     '......P.',
     '.......R',
     '..N.....',
     '........',
     '.....Q..'
]
isCheck(b)          # False
