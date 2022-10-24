# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 12:33:02 2020

@author: Alfredo
"""

# Daily Coding Problem #275

# Problem:
# The "look and say" sequence is defined as follows: beginning with the
# term 1, each subsequent term visually describes the digits
# appearing in the previous term. The first few terms are as follows:
# 1
# 11
# 21
# 1211
# 111221
# As an example, the fourth term is 1211, since the third term
# consists of one 2 and one 1.
# Given an integer N, print the Nth term of this sequence.



def lookNSay(N):
    if N == 1:
        return '1'
    
    pastSequence = '1'
    
    for step in range(1, N):
        curSequence = ''
        curDigit = pastSequence[0]
        curCnt = 1
        
        for i in range(1, len(pastSequence)):
            if pastSequence[i] == curDigit:
                curCnt+=1
            else:
                curSequence+= str(curCnt)
                curSequence+= str(curDigit)
                curCnt = 1
                curDigit = pastSequence[i]
                
        curSequence+= str(curCnt)
        curSequence+= str(curDigit)
        
        pastSequence = curSequence
        
    return curSequence


# Testing
lookNSay(5)     # '111221'
lookNSay(6)     # '312211'
