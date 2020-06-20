# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 17:20:26 2020

@author: Alfredo
"""

'''
Implement the function fib(n), 
which returns the nth number in the Fibonacci sequence, using only O(1) space.
'''

def fib(n):
    
    if n == 1:
        res = 0
    else:
        res = 1
        
    last = 0
    
    for i in range(2,n):
        tmp = res
        res+= last
        last = tmp
        
    return res
    
    
    
    
print(fib(7)) #7th number in the Fibonacci sequence is 8
