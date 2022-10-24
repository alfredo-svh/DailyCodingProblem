# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 12:23:16 2020

@author: Alfredo
"""

# Daily Coding Problem #420

# Problem:
# A number is considered perfect if its digits sum up to exactly 10.
# Given a positive integer n, return the n-th perfect number.


def perfect(n):
    # first perfect number is 19
    res = 19
    cur = 1
    
    while(cur < n):
        # we find new perfect numbers by adding 9
        res+=9
        
        # we make sure the new number is a perfect number
        s = str(res)
        t = 0
        for d in s:
            t+=int(d)
        
        # if it is, we increase the counter
        if t== 10:
            cur+=1
        
        
    return res


# -------------------------------------------------------------------
# Testing

perfect(1)          # 19
perfect(2)          # 28
perfect(29)         # 307
