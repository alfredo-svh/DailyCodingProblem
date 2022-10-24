# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 12:12:11 2020

@author: Alfredo
"""

# Daily Coding Problem # 412

# Problem:
# The "look and say" sequence is defined as follows: beginning with the term 1,
# each subsequent term visually describes the digits appearing in the previous
# term.
# As an example, the fourth term is 1211, since the third term consists of
# one 2 and one 1.
# Given an integer N, print the Nth term of this sequence.



def lookNSay(n):
    curTerm = '1'
    
    if n < 1:
        return None
    
    # we compute every term until we get our desired term
    for t in range(n-1):
        newTerm = ''
        curCount = 1
        curDigit = curTerm[0]
        
        # we go through every digit in the old term and either update the count
        # or we add the current count and digit to the term
        for d in range(1, len(curTerm)):
            if curTerm[d] == curDigit:
                curCount+=1
            else:
                newTerm += str(curCount) + str(curDigit)
                curDigit = curTerm[d]
                curCount = 1
                
        # add the last count and digit and set the new term as the current one
        newTerm+= str(curCount) + str(curDigit)
        curTerm = newTerm
    
    return int(curTerm)

# ---------------------------------------------------------------------
# Testing

lookNSay(1)         # 1
lookNSay(2)         # 11
lookNSay(3)         # 21
lookNSay(4)         # 1211
lookNSay(5)         # 111221
lookNSay(6)         # 312211
lookNSay(7)         # 13112221
