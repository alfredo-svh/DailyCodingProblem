# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:29:18 2020

@author: Alfredo
"""

# Daily Coding Problem # 386
# Problem:
# Given a string, sort it in decreasing order based on the frequency of
# characters. If there are multiple possible solutions, return any of them.

from collections import Counter

def sort(s):
    mp = Counter(s)
    res = ''
    
    for l, c in mp.most_common():
        res += l * c
        
    return res


sort('tweet')       # 'tteew'
