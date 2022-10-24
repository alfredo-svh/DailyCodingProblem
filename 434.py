# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:43:47 2021

@author: Alfredo
"""

#  Daily Coding Problem #434

# Problem:
# Given a binary search tree, find the floor and ceiling of a given integer.
# The floor is the highest element in the tree less than or equal to
# an integer, while the ceiling is the lowest element in the tree greater than
# or equal to an integer.
# If either value does not exist, return None.
        

def floor(node, target, curFloor):
    if target == node.v:
        return target
    
    if node.v > target:
        if not node.left:
            return curFloor
        return floor(node.left, target, curFloor)
    
    if curFloor == None or node.v > curFloor:
        curFloor = node.v
        
    if not node.right:
        return curFloor
    
    return floor(node.right, target, curFloor)


def ceiling(node, target, curCeil):
    if target == node.v:
        return target

    if node.v < target:
        if not node.right:
            return curCeil
        return ceiling(node.right, target, curCeil)
    
    if curCeil == None or node.v < curCeil:
        curCeil = node.v
        
    if not node.left:
        return curCeil
    
    return ceiling(node.left, target, curCeil)
    

def floorAndCeil(root, n):
    fl = floor(root, n, None)
    cl = ceiling(root, n, None)
    
    if not cl or not fl:
        return None
    
    return (fl, cl)

# ----------------------------------------------------------
# Testing
    
class Node:
    def __init__(self, val, l = None, r = None):
        self.v = val
        self.left = l
        self.right = r
        
# bst used for testing: https://bit.ly/3oMhCQe
bst = Node(15, Node(13, Node(12, Node(10, Node(9), Node(11))), Node(14)),
           Node(20, Node(18), Node(22, Node(21), Node(23))))

print(floorAndCeil(bst, 8))         # None
print(floorAndCeil(bst, 24))        # None
print(floorAndCeil(bst, 19))        # (18, 20)
print(floorAndCeil(bst, 10))        # (10, 10)
