# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:50:17 2020

@author: Alfredo
"""
#    Daily Coding Problem #258

#    In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".
#    
#    Given a binary tree, write an algorithm to print the nodes in boustrophedon order.
#    
#    For example, given the following tree:
#    
#           1
#        /     \
#      2         3
#     / \       / \
#    4   5     6   7
#    
#    You should return [1, 3, 2, 4, 5, 6, 7].


class Node():
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None
        
           
# Returns the height of a certain node (leaves have height 0)
def height(n):
    h = 0
    
    while n != None:
        n = n.left
        h+=1
    
    return h


# Helper function that returns a list of the nodes in a certain height ordered
# in order or in reverse accordingly
def helper(n, i,b,  res):
    if n == None:
        return 
    
    if i==0:
        res.append(n.val)
        
    else:
        #reverse
        if b:
            helper(n.right, i-1,b, res)
            helper(n.left, i-1, b,res)
        #in order
        else:
            helper(n.left, i-1, b,res)
            helper(n.right, i-1, b,res)
        
    return res
    

# Main function
def boustrophedon(tree):
    h = height(root)
    res = []
    
    for i in range(h):
        b = i%2
        res+=helper(root, i,b,  [])
    
    return res


# Test
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.left.left.left = Node(8) 
root.left.left.right = Node(9) 
root.left.right.left = Node(10) 
root.left.right.right = Node(11) 
root.right.left.left = Node(12) 
root.right.left.right = Node(13) 
root.right.right.left = Node(14) 
root.right.right.right = Node(15) 
root.left.left.left.left = Node(16) 
root.left.left.left.right = Node(17) 
root.left.left.right.left = Node(18) 
root.left.left.right.right = Node(19) 
root.left.right.left.left = Node(20) 
root.left.right.left.right = Node(21) 
root.left.right.right.left = Node(22) 
root.left.right.right.right = Node(23) 
root.right.left.left.left = Node(24) 
root.right.left.left.right = Node(25) 
root.right.left.right.left = Node(26) 
root.right.left.right.right = Node(27) 
root.right.right.left.left = Node(28) 
root.right.right.left.right = Node(29) 
root.right.right.right.left = Node(30) 
root.right.right.right.right = Node(31) 

boustrophedon(root)
# Returns: 
# [1, 3, 2, 4, 5, 6, 7, 15, 14, 13, 12, 11, 10, 9, 8, 16, 17, 18, 19, 20, 21, 
#        22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
