# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 22:47:20 2021

@author: Alfredo
"""


# Daily Coding Problem #438

# Problem:
# Implement a stack API using only a heap. A stack implements the following methods:
# - push(item), which adds an element to the stack
# - pop(), which removes and returns the most recently added element
#   (or throws an error if there is nothing on the stack)


import heapq

class Stack:
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        
    def push(self, item):
        heapq.heappush(self.heap, (- len(self.heap), item))
        
    def pop(self):
        if len(self.heap) == 0:
            print("Error")
        else:
            heapq.heappop(self.heap)
        

# ---------------------------------------------------------------------
# Testing
            
def show(stack):
    return [x[1] for x in stack.heap]
        

st = Stack()

st.push('a')
st.push('g')
st.push('b')
st.push('z')
st.push('d')
st.pop()
show(st)        # ['z', 'b', 'g', 'a']
st.pop()
show(st)        # ['b', 'a', 'g']
st.pop()
show(st)        # ['g', 'a']
st.pop()
show(st)        # ['a']
