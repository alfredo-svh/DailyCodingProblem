# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:18:16 2020

@author: Alfredo
"""

# Daily Coding Problem #262

# Problem:
# A bridge in a connected (undirected) graph is an edge that, if removed,
# causes the graph to become disconnected. Find all the bridges in a graph.


# helper function which returns true if all vertices have been visited
def isConnected(graph, curVertex, visited):
    if curVertex not in visited:
        visited.append(curVertex)
    
        for e in range(len(graph)):
            if graph[curVertex][e] == 1:
                graph[e][curVertex] = 0
                isConnected(graph, e, visited)
    
    
    return len(visited) == len(graph)
    

# main algorithm function which sequentially and individually deletes 
# each edge and adds that edge to the result list if the graph is not connected
# as a result of the deletion
def bridges(graph):
    res = []
    
    for a in range(len(graph)-1):
        for b in range(a+1, len(graph)):
            if graph[a][b] ==1:
                newGraph = list(map(list, graph))
                newGraph[a][b] = 0
                newGraph[b][a] = 0
                if not isConnected(newGraph, 0, []):
                    res.append((a,b))
    
    
    return res
            

# Testing
g = [[0,0,1,0,0],[0,0,0,1,0],[1,0,0,0,1], [0,1,0,0,1], [0,0,1,1,0]]
bridges(g)      # [(0, 2), (1, 3), (2, 4), (3, 4)]

g = [[0,1,1,0,0],[1,0,0,1,0],[1,0,0,0,1], [0,1,0,0,1], [0,0,1,1,0]]
bridges(g)      # []

g = [[0,0,1,1,0],[0,0,0,1,0],[1,0,0,0,1], [1,1,0,0,1], [0,0,1,1,0]]
bridges(g)      # [(1,3)]
