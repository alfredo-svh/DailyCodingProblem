# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 19:45:27 2021

@author: Alfredo
"""


# Daily Coding Problem #437

# Problem:
# Given a string and a set of characters, return the shortest substring
# containing all the characters in the set.


# returns true if the substring contains all of the characters in the set
def checkSubstring(sub, chars):
    charSet = set(chars)
    
    for c in sub:
        if c in charSet:
            charSet.remove(c)
            
    return len(charSet) == 0


def shortestSubstring(s, chars):
    strlen = len(s)
    charlen = len(chars)
    
    shortest = None
    shortestStr = ''
    
    if strlen < charlen:
        return None
    
    # we check every substring for the complete inclusion of the characters
    # and remember the shortest substring that works
    for i in range(strlen - charlen + 1):
        for j in range(i + charlen -1, strlen):
            sub = s[i:j+1]
            
            if checkSubstring(sub, chars):
                if shortest == None or j-i + 1 < shortest:
                    shortest = j-i + 1
                    shortestStr = sub
                
    return shortestStr
    


shortestSubstring('icea', 'aeci')               # 'icea'
shortestSubstring('figehaeci', 'aeci')          # 'aeci'
shortestSubstring('ADOBECODEBANC', 'ABC')       # 'BANC'
shortestSubstring('a', 'a')                     # 'a'
