# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:45:33 2020

@author: Alfredo
"""

'''
    Implement a PrefixMapSum class with the following methods:

    insert(key: str, value: int): Set a given key's value in the map. 
        If the key already exists, overwrite the value.
    sum(prefix: str): Return the sum of all values of keys that begin
        with a given prefix.

    For example, you should be able to run the following code:
    
    mapsum.insert("columnar", 3)
    assert mapsum.sum("col") == 3
    
    mapsum.insert("column", 2)
    assert mapsum.sum("col") == 5
'''




class Node:
    def __init__(self):
        self.word = ""
        self.children = {}

class Trie:

    def __init__(self):

        self.root = Node()


    def insert(self, word: str) -> None:

        nd = self.root

        for i in range(len(word)):
            if word[i] not in nd.children:
                nd.children[word[i]] = Node()

            nd = nd.children[word[i]]

        nd.word = word
    
    
    def searchHelper(self, nd, res):
        if nd.word != "":
            res.append(nd.word)
        
        for k, v in nd.children.items():
            self.searchHelper(v, res)
            
        
        return res
        
    
    
    def search(self, prefix):
        nd = self.root
        res = []
        
        for i in range(len(prefix)):
            if prefix[i] not in nd.children:
                return res
            nd = nd.children[prefix[i]]
        
        
        return self.searchHelper(nd, res)
        
        

class PrefixMapSum:
    def __init__(self):
        self.mp = {}
        self.trie = Trie()
    
    def insert(self, key, value):
        self.mp[key] = value
        self.trie.insert(key)
        
    def sum(self, prefix):
        sm = 0
        keys = self.trie.search(prefix)
        
        for key in keys:
            sm += self.mp[key]
        
        return sm
    
    
mapsum = PrefixMapSum()
    
mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
