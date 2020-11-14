# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:14:48 2020

@author: Alfredo
"""

# Daily Coding Problem #380

# Problem:
# Implement integer division without using the division operator. Your
# function should return a tuple of (dividend, remainder) and it should take
# two numbers, the product and divisor.

def divide(prod, divisor):
    if divisor == 0:
        return 'Error'
    
    if prod < divisor:
        return (0,prod)
    
    dividend = 1
    res = divisor
    
    while res + divisor <= prod:
        dividend+=1
        res += divisor
        
    return (dividend, prod - res)
    
    
# ----------------------------------
# Testing:
    
divide(10, 3)           # (3, 1)
divide(3, 0)            # 'Error'
divide(4, 8)            # (0, 4)
divide(31, 31)          # (1,0)
divide(812, 11)         # (73, 9)
