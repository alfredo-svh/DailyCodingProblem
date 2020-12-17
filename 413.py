# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 11:30:06 2020

@author: Alfredo
"""

# Daily Coding Challenge #413

# Problem:
# There exists a staircase with N steps, and you can climb up either 1 or 2
# steps at a time. Given N, write a function that returns the number of unique
# ways you can climb the staircase. The order of the steps matters.

# What if, instead of being able to climb 1 or 2 steps at a time, you could
# climb any number from a set of positive integers X? For example, if
# X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.


# Recursive function that climbs the ladder until it reaches the top
# If it does so in a unique series of steps at a time, it's added to the result
def helper(n, x, curStep, curArr, finalArr):
    if curStep >= n:
        if curStep == n and curArr not in finalArr:
            finalArr.append(curArr)
        return finalArr
    
    # recursively simulate for every "steps at a time" I can take
    for i in x:
        steps = curArr.copy()
        steps.append(i)
        finalArr = helper(n, x, curStep + i, steps, finalArr)
    
    return finalArr


def staircase(n, x):
    if n< 1:
        return None
    if n == 1:
        return [[1]]
    
    return helper(n, x, 0, [], [])


# -----------------------------------------------------------------
# Testing

staircase(4, {1, 2})             
# [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]

staircase(4, {1, 2, 3})          
# [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]]

staircase(5, {1, 2, 5})
# [[1, 1, 1, 1, 1],
# [1, 1, 1, 2],
# [1, 1, 2, 1],
# [1, 2, 1, 1],
# [1, 2, 2],
# [2, 1, 1, 1],
# [2, 1, 2],
# [2, 2, 1],
# [5]]
