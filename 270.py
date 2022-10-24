# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 18:07:43 2020

@author: Alfredo
"""

# Daily Coding Problem #270

# Problem:
# A network consists of nodes labeled 0 to N. You are given a list of
# edges (a, b, t), describing the time t it takes for a message
# to be sent from node a to node b. Whenever a node receives a
# message, it immediately passes the message on to a neighboring
# node, if possible.
# Assuming all nodes are connected, determine how long it will take for
# every node to receive a message that begins at node 0. 


#recursive helper function. Returns the shortest time possible to get to the
#target node from node 0
def helper(node, edges):
    if node == 0:
        return 0
    
    shortestTime = None
    
    #for each possible way to get to the current node, use recursion to get
    #the time it takes to reach it from node 0 and keep the shortest one
    for i in range(len(edges)):
        if edges[i][1] == node:
            time = edges[i][2] + helper(edges[i][0], edges)
            if shortestTime == None or time < shortestTime:
                shortestTime = time
                    
    return shortestTime


def time(edges, N):
    totalTime = 0
        
    for i in range(N):
        totalTime = max(totalTime, helper(i+1, edges))

    return totalTime
    


# Testing:
edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]

time(edges, 5)     # 9
