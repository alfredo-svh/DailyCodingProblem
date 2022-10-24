# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 12:35:38 2020

@author: Alfredo
"""

# Daily Coding Problem #376

# Problem:
# You are writing an AI for a 2D map game. You are somewhere in a 2D grid, and
# there are coins strewn about over the map.
# Given the position of all the coins and your current position, find the
# closest coin to you in terms of Manhattan distance. That is, you can move
# around up, down, left, and right, but not diagonally. If there are multiple
# possible closest coins, return any of them.
# For example, given the following map, where you are x, coins are o, and empty
# spaces are . (top left is 0, 0):
# ---------------------
# | . | . | x | . | o |
# ---------------------
# | o | . | . | . | . |
# ---------------------
# | o | . | . | . | o |
# ---------------------
# | . | . | o | . | . |
# ---------------------
# return (0, 4), since that coin is closest.


def closestCoin(pos, coins):
    minDist = -1
    
    for coin in coins:
        curDist = abs(coin[0] - pos[0]) + abs(coin[1]-pos[1])
        
        if minDist < 0 or curDist < minDist:
            minDist = curDist
            closest = coin
    
    return closest



closestCoin((0,2), [(0, 4), (1, 0), (2, 0), (3, 2)])        # (0,4)
