# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 17:44:21 2021

@author: Alfredo
"""


# Daily Coding Problem #435

# Problem:
# Given pre-order and in-order traversals of a binary tree, write
# a function to reconstruct the tree.



def helper(po, io):
    # the first value in preorder will be our next node
    newNode = Node(po.pop(0))
    
    # split the inorder values at the current node to get
    # the values on its left and right branches, respectively
    l, r = io.split(newNode.val)
    
    # recursive calls to construct its left and right branches
    if l != '':
        newNode.left = helper(po, l)
    if r != '':
        newNode.right = helper(po, r)
    
    return newNode
    

def reconstruct(po, io):
    newPo = po.copy()
    
    # the root of the tree will be the first value in preorder
    root = Node(newPo.pop(0))
    
    # split the inorder sequence at the current node
    # to get the values on its left and right branches respectively
    l, r = ''.join(io).split(root.val)
    
    
    root.left = helper(newPo, l)
    root.right = helper(newPo, r)
    
    return root


# ---------------------------------------------------------------------------
# Testing

class Node:
    def __init__(self, v, r = None, l = None):
        self.val = v
        self. left = l
        self.right = r
        
# returns a string containing the values of the tree in preorder
def preorder(nd):
    s = nd.val
    
    if nd.left:
        s+=preorder(nd.left)
        
    if nd.right:
        s+=preorder(nd.right)
        
    return s


# returns a string containing the values of the tree in inorder
def inorder(nd):
    s = ''
    
    if nd.left:
        s += inorder(nd.left)
        
    s+= nd.val
    
    if nd.right:
        s += inorder(nd.right)
        
    return s



po = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
io = ['d', 'b', 'e', 'a', 'f', 'c', 'g']

tree = reconstruct(po, io)

list(preorder(tree)) == po          # True
list(inorder(tree)) == io           # True
