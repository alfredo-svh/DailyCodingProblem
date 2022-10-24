# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 12:45:35 2020

@author: Alfredo
"""

# Daily Coding Problem #422

# Problem:
# Write a program to merge two binary trees. Each node in the new tree should
# hold a value equal to the sum of the values of the corresponding nodes of
# the input trees.
# If only one input tree has a node in a given position, the corresponding
# node in the new tree should match that input node.


# Binary Tree Node class
class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


# Recursive helper function to merge the binary trees
def dfs(t1, t2, nt):
    # setting variables
    if t1 == None:
        left1 = None
        right1 = None
    else:
        left1 = t1.left
        right1 = t1.right
    if t2 == None:
        left2 = None
        right2 = None
    else:
        left2 = t2.left
        right2 = t2.right
        
    # setting children of new merged tree appropiately
    if left1 or left2:
        nt.left = Node((0 if left1 == None else left1.val) + (0 if left2 == None else left2.val))
    if right1 or right2:
        nt.right = Node((0 if right1 == None else right1.val) + (0 if right2 == None else right2.val))
    
    # recursive calls
    if nt.left:
        dfs(left1, left2, nt.left)
    if nt.right:
        dfs(right1, right2, nt.right)
        
        
# Main merging function that calls dfs()
def merge(t1, t2):
    newTree = Node(t1.val + t2.val)
    
    dfs(t1, t2, newTree)
    
    return newTree


# ----------------------------------------------------------------------------
# Testing


# Functions that create the two trees to be merged
def makeTree1():
    tree = Node(3)
    tree.right = Node(8)
    
    return tree

def makeTree2():
    tree = Node(3)
    tree.left = Node(5)
    tree.left.left = Node(1)
    tree.right = Node(8)
    
    return tree


# Helper function to print tree values in a pre-order manner
def printTree(t):
    print(t.val)
    if t.left:
        printTree(t.left)
    if t.right:
        printTree(t.right)


# Driver function to execute the program
def driver():
    t1 = makeTree1()
    t2 = makeTree2()
    
    printTree(merge(t1, t2))
    
    
driver()
