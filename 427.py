# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 15:19:54 2020

@author: Alfredo
"""


# Daily Coding Problem #427

# Problem:
# A competitive runner would like to create a route that starts and ends at his
# house, with the condition that the route goes entirely uphill at first, and
# then entirely downhill.
# Given a dictionary of places of the form {location: elevation}, and a
# dictionary mapping paths between some of these locations to their
# corresponding distances, find the length of the shortest route satisfying
# the condition above. Assume the runner's home is location 0.


# recursive helper function
def helper(elevs, paths, curLoc, pathLen, isDec):
    
    # when we get back home, return the total path length
    if curLoc == 0 and isDec == True:
        return pathLen
    
    curElev = elevs[curLoc]
    shortestRun = -1
    
    for path, dist in paths.items():
        if path[0] == curLoc:
            # we skip higher elevation points if we're now descending
            if elevs[path[1]] > curElev and isDec:
                continue
            
            # recursive call to function taking next path
            if (elevs[path[1]] < curElev):
                curRes = helper(elevs, paths, path[1], pathLen + dist, True)
            else:
                curRes = helper(elevs, paths, path[1], pathLen + dist, isDec)
            
            # we update the length of the shortest run
            if curRes < shortestRun or shortestRun < 0:
                shortestRun = curRes
    
    return shortestRun


def pickyRun(elevs, paths):
    
    return helper(elevs, paths, 0, 0, False)


# ----------------------------------------------------------------------------
# Testing

e = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
p = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}
pickyRun(e, p)
