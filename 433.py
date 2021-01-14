# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 10:47:15 2021

@author: Alfredo
"""


# Daily Coding Problem # 433

# Problem:
# Given an integer n, find the next biggest integer with the same number
# of 1-bits on.

# Note: current solution only accepts positive integers


def sameOnes(n):
    if n < 1:
        return n
    
    nBin = list(bin(n)[2:])
    
    f = False
    onesFlipped = -1
    
    # check first 0 (after a 1) and flip it while counting 1s
    for i in range(len(nBin)-1, -1, -1):
        if f and nBin[i] == '0':
            nBin[i] = '1'
            break
        
        # flip  the 1s to the right of first 0
        if nBin[i] == '1':
            f = True
            onesFlipped += 1
            nBin[i] = '0'
            
    # if we flipped the leftmost bit, we insert a 1 to its left
    if nBin[0] == '0':
        nBin.insert(0, '1')
            
    # switch the 0s needed to get the target number of total 1s
    # from the rightmost bit
    nBin = ''.join(nBin)
    if onesFlipped > 0:
        nBin = nBin[:-onesFlipped] + '1' * onesFlipped

    return int(nBin, 2)
    
# -----------------------------------------------------------------------------
# Testing
    
# Brute force algorithm to check correctnes
def sameOnesBF(n):
    if n < 1:
        return n
    
    newInt = n+1
    
    ones = str(bin(n)[2:]).count('1')
    
    while True:
        if str(bin(newInt)[2:]).count('1') == ones:
            return newInt
        newInt+=1


sameOnes(3)                                 # 5
sameOnes(3) == sameOnesBF(3)                # True
sameOnes(8)                                 # 16
sameOnes(8) == sameOnesBF(8)                # True
sameOnes(988784)                            # 988803
sameOnes(988784) == sameOnesBF(988784)      # True
