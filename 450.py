# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:46:54 2021

@author: Alfredo
"""


# Daily Coding Problem #450

# Problem:
# You're given a string consisting solely of (, ), and *. * can represent
# either a (, ), or an empty string.
# Determine whether the parentheses are balanced.



# recursive function that returns True if the parenthesis are balanced and
# false otherwise
def helper(s, count):
    # base case: end of string / empty string
    if s == "":
        return count == 0

    # if we ever see a ) without a matching ( first, the parenthesis are unbalanced
    if count < 0:
        return False
    
    
    # we "pop" the first character of the string
    curChar = s[0]
    
    if len(s) == 1:
        s =""
    else:
        s = s[1:]
    
    
    if curChar == '(':
        return helper(s, count+1)
    
    if curChar == ')':
        return helper(s, count-1)
    
    # if curChar is '*', we call the recursive function for each possible value
    return helper(s, count) or helper(s, count-1) or helper(count+1)
    

def isBalanced(s):
    
    return helper(s, 0)



isBalanced('(()*')      # True
isBalanced('(*)')       # True
isBalanced(')*(')       # False
