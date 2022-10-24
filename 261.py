# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:52:56 2020

@author: Alfredo
"""

# Daily Coding Problem #261

# Problem:
# Given a dictionary of character frequencies, build a Huffman tree, and
# use it to determine a mapping between characters and their encoded
# binary strings.


class Node():
    def __init__(self, c = None, cnt = 0):
        self.char = c
        self.count = cnt
        self.left = None
        self.right = None
        
        
# maps each character into its corresponding binary huffman code value
def mapCtoB(node, curBinStr, mapping):
    if node == None:
        return mapping
    if node.char != None:
        mapping[node.char] = curBinStr
    else:
        mapCtoB(node.left, curBinStr + "0", mapping)
        mapCtoB(node.right, curBinStr + "1", mapping)
        
    
    return mapping
        
      
# builds the huffman tree  
def buildTree(dct):
    # first, we sort the characters by their recurrence
    sortedDct = sorted(dct.items(), key=lambda x: x[1])
    
    treeArr = []
    
    # we start by creating an array of leaf nodes
    for item in sortedDct:
        treeArr.append(Node(item[0], item[1]))
        
    # we pop the two nodes with the least recurrence and bind them together
    # by creating a parent node and inserting it back in the array in its new place
    # until there is only one node in the array, which will be the root of
    # our Huffman Tree
    while 1:
        r = treeArr.pop()
        l = treeArr.pop()
        
        newCount = l.count + r.count
        newNode = Node(cnt = newCount)
        newNode.left = l
        newNode.right = r
        
        for i in range(len(treeArr)-1, -1, -1):
            if treeArr[i].count >= newCount:
                treeArr.insert(i+1, newNode)
                break
            if i == 0:
                treeArr.insert(0, newNode)
        
        if len(treeArr) == 0:
            treeArr.append(newNode)
            break
            

    return treeArr[0]


# main function
def huffman(dct):
    tree = buildTree(dct)
    return mapCtoB(tree, "", {})


# Testing --------------------------------------------------------------------
    
# takes a string, outputs a dictionary of character and recurrence
def charCounter(s):
    dct = {}
    for c in s:
        if c not in dct:
            dct[c] = 1
        else:
            dct[c] +=1
    
    return dct
    
s ="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum posuere felis nec varius faucibus. Sed placerat arcu id justo cursus, a vestibulum neque laoreet. Phasellus molestie, mi id mattis iaculis, elit lectus tincidunt sapien, sed elementum neque dolor in leo. Vivamus ut dui felis. Aenean sit amet accumsan lectus, id."
dct = charCounter(s)
huffman(dct)
