# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:23:44 2020

@author: Alfredo
"""

# Daily Coding Problem: Problem #254

# Problem: Recall that a full binary tree is one in which each node
# is either a leaf node, or has two children. Given a binary tree, 
# convert it to a full one by removing nodes with only one child.


class Node:
    def __init__(self, n):
        self.v = n
        self.right = None
        self.left = None


# recursive function that turns BT into a FBT
def helper(n):
    if n.right==None and n.left == None:
        return n
    
    # if node has exactly one child, we replace it with its only child
    if n.right==None or n.left==None:
        if n.left!=None:
            n = n.left
        else:
            n = n.right
        
        
        n = helper(n)
   
    else:
        n.left = helper(n.left)
        n.right = helper(n.right)
        
    
    return n
        

# For Testing: recursively print the new binary tree (preorder)
def printTree(n):
    print(n.v)
    
    if n.right==None and n.left==None:
        return
    
    if n.left==None:
        print('NoneLeftNode')
    else:
        printTree(n.left)
        
    if n.right==None:
        print('NoneRightNode')
    else:
        printTree(n.right)
    

# Main function called
def makeFullBinaryTree(root):
    fullBT = helper(root)
    
    printTree(fullBT)
    
    
    
# Test
root = Node(0)
root.left= Node(1)
root.right= Node(2)
root.left.left= Node(3)
root.left.left.right= Node(5)
#                 0
#              /     \
#            1         2
#          /       
#        3          
#          \          
#            5          

makeFullBinaryTree(root)

# Returns:
#                 0
#              /     \
#            5         2
