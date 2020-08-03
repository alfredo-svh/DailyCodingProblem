# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:57:03 2020

@author: Alfredo
"""


# Daily Coding Problem #277

# Problem:
# UTF-8 is a character encoding that maps each symbol to one, two,
# three, or four bytes.
# For example, the Euro sign, €, corresponds to the three bytes
# 11100010 10000010 10101100. The rules for mapping
# characters are as follows:
#  - For a single-byte character, the first bit must be zero.
#  - For an n-byte character, the first byte starts with n ones and a
#    zero. The other n - 1 bytes all start with 10.
# Visually, this can be represented as follows.
#  Bytes   |           Byte format
# -----------------------------------------------
#    1     | 0xxxxxxx
#    2     | 110xxxxx 10xxxxxx
#    3     | 1110xxxx 10xxxxxx 10xxxxxx
#    4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
# Write a program that takes in an array of integers representing byte
# values, and returns whether it is a valid UTF-8 encoding. 



def utf8(arr):
    n = len(arr)
    if n < 1 or n > 4:
        return False
    
    
    bts = []
    
    #take the binary representations of the integers
    for i in range(n):
        if arr[i] >=0 and arr[i] <= 255:
            bts.append(format(arr[i], '08b'))
        else:
            return False
    
    
    if n ==1:
        return bts[0][0] == '0'
    
    #validating first byte
    for i in range(n):
        if bts[0][i] == '0':
            return False
    
    if bts[0][n]=='1':
        return False
    
    #validating the rest of the bytes
    for i in range(1, n):
        if bts[i][0] != '1' or bts[i][1] != '0':
            return False
    
    return True



# Testing
utf8([226, 130, 172])       # True
utf8([226, 194, 172])       # False
utf8([226])     # False
utf8([100])     # True
utf8([194, 130])    # True
