# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 11:34:26 2020

@author: Alfredo
"""

# Daily Coding Problem #416
# Problem:
# You are in an infinite 2D grid where you can move in any of the 8 directions.
# You are given a sequence of points and the order in which you need to cover
# the points. Give the minimum number of steps in which you can achieve it.
# You start from the first point.


def moves(arr):
    totMoves = 0
    
    for i in range(1, len(arr)):
        x = abs(arr[i][0] -arr[i-1][0])
        y = abs(arr[i][1] - arr[i-1][1])
        totMoves += max(x,y)
        
    return totMoves

# -------------------------------------------
# Testing

moves([(0, 0), (1, 1), (1, 2)])         # 2
moves([(0, 0), (3, 3), (5, 3)])         # 5
moves([(0, 0), (1, 5), (1, 2)])         # 8
moves([(0, 0), (-1, -1), (-1, -2)])     # 2
moves([(0, 0), (-3, -3), (-5, -3)])     # 5
moves([(0, 0), (1, -1), (-1, 2)])       # 4
