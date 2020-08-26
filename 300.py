# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:06:48 2020

@author: Alfredo
"""

# Daily Coding Problem #300

# Problem:
# On election day, a voting machine writes data in the form
# (voter_id, candidate_id) to a text file. Write a program that
# reads this file as a stream and returns the top 3 candidates at any
# given time. If you find a voter voting more than once, report this as fraud.


import heapq

def topThreeCandidates(fname):
    #read file contents
    f=open(fname, "r")
    f1 = f.readlines()
    f.close()
    
    candidates = {}
    voters = set()
    
    for line in f1:
        voter = line[1:-1].split(', ')[0]
        candidate = line[1:-1].split(', ')[1]
    
        if voter in voters:
            return "FRAUD!"
        else:
            voters.add(voter)
        
        if candidate in candidates:
            candidates[candidate]+=1
        else:
            candidates[candidate] = 1
            
    return heapq.nlargest(3, candidates.keys(), key= lambda x: candidates[x])


# Testing:
topThreeCandidates('test.txt')

# In:
#(voter1, candidate1)
#(voter2, candidate1)
#(voter3, candidate2)
#(voter4, candidate2)
#(voter5, candidate3)
#(voter6, candidate3)
#(voter12, candidate4)
#(voter7, candidate4)
#(voter8, candidate4)
#(voter9, candidate4)
#(voter10, candidate2)
#(voter11, candidate1)
# Out:
#['candidate4)', 'candidate2)', 'candidate1)']

# In:
#(voter1, candidate1)
#(voter2, candidate1)
#(voter3, candidate2)
#(voter2, candidate2)
#(voter5, candidate3)
# Out:
#'FRAUD!'