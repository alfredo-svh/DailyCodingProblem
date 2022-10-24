# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 23:18:28 2021

@author: Alfredo
"""


# Daily Coding Problem #439

# Problem:
# Given an unordered list of flights taken by someone, each represented as
# (origin, destination) pairs, and a starting airport, compute the person's
# itinerary. If no such itinerary exists, return null. If there are multiple
# possible itineraries, return the lexicographically smallest one.
# All flights must be used in the itinerary.


def helper(curAP, flights, curItinerary, res):
    # base case: all flights have been used in the itinerary
    # we add the itinerary to our results
    if len(flights) == 0:
        res.append(curItinerary)
        return
    
    # we recursively go through every possible flight, creating the itinerary
    for i in range(len(flights)):
        if flights[i][0] == curAP:
            ci = curItinerary.copy()
            fl = flights.copy()
            
            ci.append(flights[i][1])
            del fl[i]
            
            helper(ci[-1], fl, ci, res)
            

def itinerary(flights, start):
    res = []
    
    helper(start, flights, [start], res)
    
    # return null if the itinerary is less than two flights
    if len(res) == 0:
        return None
    
    # return the one itinerary
    if len(res) == 1:
        return res[0]
    
    # return lexicographically smaller one
    return min(res)

# ---------------------------------------------------------------------------------
# Testing


itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL')
# ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM')
# None
itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A')
# ['A', 'B', 'C', 'A', 'C']
