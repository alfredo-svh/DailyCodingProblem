# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 18:07:43 2020

@author: Alfredo
"""

# Daily Coding Problem #272

# Problem:
# Write a function, throw_dice(N, faces, total), that
# determines how many ways it is possible to throw N dice with some
# number of faces each to get a specific total.


# recursive function
def helper(N, roll_vals, total):
    #if out of dice or over the target, we don't add to the count
    if N < 1 or total  < 1:
        return 0
    
    #if we have one dice left and a possibility to roll the value needed to
    #reach total, we add to the count
    if N == 1 and total in roll_vals:
        return 1
    
    res = 0
    
    # recursively check every possible dice roll
    for face in roll_vals:
        res+= helper(N-1, roll_vals, total - face)
    
    return res


def throw_dice(N, faces, total):
    #make a list with the face values
    roll_vals = []
    for i in range(faces):
        roll_vals.append(i+1)
    
    return helper(N, roll_vals, total)



# Testing
throw_dice(3, 6, 7)     # 15
