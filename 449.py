# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:46:27 2021

@author: Alfredo
"""


# Daily Coding Problem # 449

# Problem:
# Given an even number (greater than 2), return two prime numbers whose sum
# will be equal to the given number.
# If there are more than one solution possible, return the lexicographically
# smaller solution.


import sympy


def primeSum(n):
    if n < 4:
        return None
    if n % 2 != 0:
        return None
    
    if n == 4:
        return (2,2)
    
    a = 3
    b = n-3
    
    while 1:
        if sympy.isprime(a) and sympy.isprime(b):
            return (a, b)
        
        a+=2
        b-=2
        
        
primeSum(8)         # (3, 5)
primeSum(30)        # (7, 23)
primeSum(238)       # (5, 233)
primeSum(3790)      # (11, 3779)
primeSum(704632)    # (29, 704603)
