# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 10:26:18 2020

@author: Alfredo
"""

# Daily Coding Problem #301

# Problem:
# Implement a data structure which carries out the following operations
# without resizing the underlying array:
#     add(value): Add a value to the set of values.
#     check(value): Check whether a value is in the set.
# The check method may return occasional false positives (in other
# words, incorrectly identifying an element as part of the set), but should
# always correctly identify a true element.

class StaticArray():
    def __init__(self):
        self.arr = 0
    
    
    def add(self, val):
        self.arr |= val
    
    
    def check(self, val):
        if val == self.arr & val:
            return True
        
        return False


# Testing
sa = StaticArray()
sa.add(2)
sa.add(4)
sa.add(8)
sa.add(10)

sa.check(4)     # True
sa.check(10)    # True
sa.check(6)     # True       [False positive]
sa.check(5)     # False
sa.check(11)    # False
sa.check(17)    # False
