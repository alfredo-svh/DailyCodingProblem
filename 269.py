# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 17:25:38 2020

@author: Alfredo
"""

# Daily Coding Problem #269

# Problem:
# You are given an string representing the initial conditions of some
# dominoes. Each element can take one of three values:

# - 'L', meaning the domino has just been pushed to the left,
# - 'R', meaning the domino has just been pushed to the right, or
# - '.', meaning the domino is standing still.

# Determine the orientation of each tile when the dominoes stop falling.
# Note that if a domino receives a force from the left and right side
# simultaneously, it will remain upright.



def helper(arr):
    res = []
    changes = 0
    
    for i in range(len(arr)):
        if arr[i] == '.':
            #special case: first
            if i == 0:
                if arr[i+1] =='L':
                    res.append('L')
                    changes +=1
                    continue
                    
            #special case: last
            elif i==len(arr)-1:
                if arr[i-1] == 'R':
                    res.append('R')
                    changes+=1
                    continue
                
            #check if it's falling to the right
            elif arr[i-1] == 'R' and arr[i+1]!= 'L':
                res.append('R')
                changes+=1
                continue
            
            #check if it's falling to the left
            elif arr[i+1] == 'L' and arr[i-1]!='R':
                res.append('L')
                changes+=1
                continue
            
        res.append(arr[i])
    
    #continue until there are no more changes to be made
    if changes ==0:
        return res
    else:
        return helper(res)


def orientation(s):
    if len(s) < 2:
        return s
    return ''.join(helper(list(s)))
    


# Testing
s = '.L.R....L'
orientation(s)      # 'LL.RRRLLL'

s = '..R...L.L'
orientation(s)      # '..RR.LLLL'
