# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:46:47 2021

@author: Alfredo
"""


# Daily Coding Problem # 452

# Problem:
# Let's represent an integer in a linked list format by having each node
# represent a digit in the number. The nodes make up the number in
# reversed order.
# Given two linked lists in this format, return their sum in the same
# linked list format.



class Node:
    def __init__(self, v, nx = None):
        self.val = v
        self.next = nx
  
      
# takes the head node of a linked list and returns the integer represented
# in the linked list
def toInt(nd):
    num = nd.val
    exp = 10
    
    nd = nd.next
    
    while nd != None:
        num += nd.val * exp
        
        nd = nd.next
        exp *=10
        
    return num


# takes an integer and returns a linked list representation of the integer
# as detailed above
def toLinkedList(num):
    strnum = str(num)
    
    head = Node(int(strnum[-1]))
    nd = head
    
    for i in range(len(strnum)-2, -1, -1):
        nd.next = Node(int(strnum[i]))
        nd = nd.next
        
    return head
        


def plus(n1, n2):
    if not n1 or not n2:
        return
    
    integerSum = toInt(n1) + toInt(n2)
    
    return toLinkedList(integerSum)


# ----------------------------------------------------------------------------
# Testing

n1 = Node(9, Node(9)) # 9->9 (99)
n2 = Node(5, Node(2)) # 5->2 (25)

lnklst = plus(n1, n2) # 99 + 25 = 124: 4->2->1

toInt(lnklst)           # 124
