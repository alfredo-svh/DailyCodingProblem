# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 16:12:19 2021

@author: Alfredo
"""


# Daily Coding Problem #443

# Problem:
# Implement a queue using two stacks. Recall that a queue is a FIFO
# (first-in, first-out) data structure with the following methods:
# - enqueue, which inserts an element into the queue, and
# - dequeue, which removes it.



class Queue:
    def __init__(self):
        # dequeue ready
        self.s1 = []
        # new enqueues
        self.s2 = []
        
        
    def enqueue(self, val):
        self.s2.append(val)
        
        
    def dequeue(self):
        if not self.s1 and not self.s2:
            return None
        
        # if s1 is empty, transfer all the elements in s2 into s1
        # in dequeue-ready order
        if not self.s1:
            while self.s2:
                self.s1.append(self.s2.pop())
            
        # pop from dequeue-ready s1
        return self.s1.pop()
    
    
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.dequeue()         # 1
q.dequeue()         # 2
q.dequeue()         # 3
q.dequeue()         # 4
q.dequeue()         # 5
q.dequeue()         # None

q.enqueue('a')
q.enqueue('b')
q.dequeue()         # 'a'  
q.enqueue('c')
q.dequeue()         # 'b'
q.dequeue()         # 'c'
q.dequeue()         # None
