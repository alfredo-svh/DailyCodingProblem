# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 23:22:41 2020

@author: Alfredo
"""

# Daily Coding Problem #378

# Problem:
# Write a function that takes in a number, string, list, or dictionary and
# returns its JSON encoding. It should also handle nulls.


def helperDict(dct):
    json = ''
    
    for k, v in dct.items():
        json += jsonify(k) + ": "
        json += jsonify(v) + ", "
        
    return json[:-2]


def helperList(lst):
    json = ''
    
    for v in lst:
        json += jsonify(v) + ", "
        
    return json[:-2]


def jsonify(ip):  
    
    if type(ip) is int or type(ip) is float:
        return str(ip)
    
    elif type(ip) is str:
        return '"' + ip + '"'
        
    elif type(ip) is list:
        return '[' + helperList(ip) + ']'
    
    elif type(ip) is dict:
        return '{' + helperDict(ip) + '}'
    
    else:
        return 'null'
                
           
# ----------------------------------------------------
# Testing
    
jsonify([None, 123, ["a", "b"], {"c":"d"}])     # '[null, 123, ["a", "b"], {"c": "d"}]'
jsonify(None)                                   # 'null'
jsonify(334.23)                                 # '334.23'
jsonify("Test")                                 # '"Test"'
jsonify({"a": [1,2,3], "b": [4,5,6]})           # '{"a": [1, 2, 3], "b": [4, 5, 6]}'
