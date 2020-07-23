# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:51:00 2020

@author: Alfredo
"""

# Daily Coding Problem #267

# Problem:
# You are presented with an 8 by 8 matrix representing the positions of pieces
# on a chess board. The only pieces on the board are the black king and various
# white pieces. Given this matrix, determine whether the king is in check.



#checks in sraight lines for a queen or a rook
def checkRook(board, posI, posJ):
    #up
    i= posI-1
    while(i>=0):
        if board[i][posJ] != '.':
            if board[i][posJ] == 'R' or board[i][posJ] == 'Q':
                return True
            else:
                break
        i-=1
        
    #down
    i= posI+1
    while(i<=7):
        if board[i][posJ] != '.':
            if board[i][posJ] == 'R' or board[i][posJ] == 'Q':
                return True
            else:
                break
        i+=1
    
    
    #left
    j= posJ-1
    while(j>=0):
        if board[posI][j] != '.':
            if board[posI][j] == 'R' or board[posI][j] == 'Q':
                return True
            else:
                break
        j-=1
        
    #right
    j= posJ+1
    while(i<=7):
        if board[posI][j] != '.':
            if board[posI][j] == 'R' or board[posI][j] == 'Q':
                return True
            else:
                break
        j+=1
    
    return False


#checks in diagonals for a bishop or queen or a pawn
def checkBishop(board, posI, posJ):
    #right, up
    i= posI-1
    j=posJ+1
    while i >=0 and j<=7:
        if board[i][j] != '.':
            if board[i][j] == 'B' or board[i][j] == 'Q':
                return True
            else:
                break
        i-=1
        j+=1
        
    #left, up
    i= posI-1
    j=posJ-1
    while i >=0 and j>=0:
        if board[i][j] != '.':
            if board[i][j] == 'B' or board[i][j] == 'Q':
                return True
            else:
                break
        i-=1
        j-=1
        
    #right, down
    i= posI+1
    j=posJ+1
    while i <=7 and j<=7:
        if board[i][j] != '.':
            if board[i][j] == 'B' or board[i][j] == 'Q' or (i==posI+1 and board[i][j] == 'P'):
                return True
            else:
                break
        i+=1
        j+=1
        
    #left, down
    i= posI+1
    j=posJ-1
    while i <=7 and j>=0:
        if board[i][j] != '.':
            if board[i][j] == 'B' or board[i][j] == 'Q' or (i==posI+1 and board[i][j] == 'P'):
                return True
            else:
                break
        i+=1
        j-=1
    
    return False


#checks for a knight
def checkKnight(board, posI, posJ):
    if posI>=2 and posJ>=1:
        if board[posI-2][posJ-1] == 'N':
            return True
    
    if posI>=1 and posJ>=2:
        if board[posI-1][posJ-2] == 'N':
            return True
        
    if posI>=2 and posJ<=6:
        if board[posI-2][posJ+1] == 'N':
            return True
        
    if posI>=1 and posJ<=5:
        if board[posI-1][posJ+2] == 'N':
            return True
        
    if posI<=6 and posJ>=2:
        if board[posI+1][posJ-2] == 'N':
            return True
        
    if posI<=5 and posJ>=1:
        if board[posI+2][posJ-1] == 'N':
            return True
        
    if posI<=5 and posJ<=6:
        if board[posI-2][posJ-1] == 'N':
            return True
        
    if posI<=6 and posJ<=5:
        if board[posI-1][posJ-2] == 'N':
            return True
    
    return False


# looks for the king and then checks whether another piece has it on Check
def isInCheck(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'K':
                return checkRook(board, i, j) or checkBishop(board, i, j) or checkKnight(board, i, j)
    
    return False
    

# Testing
board = [['.','.','.','K','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','B','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','P','.'],
        ['.','.','.','.','.','.','.','R'],
        ['.','.','N','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','Q','.','.']]

isInCheck(board)        # True
