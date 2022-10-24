# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:17:36 2021

@author: Alfredo
"""


# Daily Coding Problem #442

# Problem:
# A Cartesian tree with sequence S is a binary tree defined by the following
# two properties:
# 1. It is heap-ordered, so that each parent value is strictly less than
#   that of its children.
# 2. An in-order traversal of the tree produces nodes with values that
#   correspond exactly to S.
# 
# Given a sequence S, construct the corresponding Cartesian tree.


class Node:
    def __init__(self, v, l = None, r= None):
        self.val = v
        self.left = l
        self.right = r


# helper function takes a preorder and inorder lists and recursively creates
# a tree
def helper(pre, ino):
    # our next node is the first value in our preorder (sorted) list
    nd = Node(pre.pop(0))
    
    l = []
    r = []
    
    # we look for our next node in the inorder list and divide it in two:
    # values for the left branch and values for the right branch
    for i in range(len(ino)):
        if ino[i] == nd.val:
            l = ino[:i]
            r = ino[i+1:]
    
    # recursively create the left and right branches
    if len(l) > 0:
        nd.left = helper(pre, l)
        
    if len(r) > 0:
        nd.right = helper(pre, r)
    
    return nd


# our driver function takes a sequence, creates our preorder and inorder lists
# to pass as arguments for our recursive helper function and it returns the
# root node of the cartesian tree created
def cartesian(s):
    pre = sorted(s)
    ino = s.copy()
    
    return helper(pre, ino)


# ----------------------------------------------------------------------------
# Testing

# returns a list of the values in a tree in-order
def inorder(nd, res):
    
    if nd.left:
        inorder(nd.left, res)
        
    res.append(nd.val)
    
    if nd.right:
        inorder(nd.right, res)
    
    return res


# returns true if the tree is heap oriented and false otherwise
def isHeapOriented(nd):
    
    l = True
    r = True
    
    if nd.left:
        if nd.left.val <= nd.val:
            return False
        l = isHeapOriented(nd.left)
        
    if nd.right and l:
        if nd.right.val <= nd.val:
            return False
        r = isHeapOriented(nd.right)
        
    return l and r



seq = [3, 2, 6, 1, 9]
tree = cartesian(seq)

isHeapOriented(tree)            # True
inorder(tree, []) == seq        # True
