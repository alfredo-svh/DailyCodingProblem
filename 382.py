# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:13:53 2020

@author: Alfredo
"""

# Daily Coding Problem # 382

# Problem:
# Yesterday you implemented a function that encodes a hexadecimal
# string into Base64.
# Write a function to decode a Base64 string back to a hexadecimal string.


def b64ToHex(b64Str):
    binStr = ''
    padding = 0
    
    # we get the 6 bit binary representation of each base64 character
    for c in b64Str:
        # a-z
        if c >= 'a':
            binStr += bin(ord(c) - 71)[2:].zfill(6)
        # A-Z
        elif c >= 'A':
            binStr += bin(ord(c) - 65)[2:].zfill(6)
        # =
        elif c == '=':
            padding += 1
        # 0-9
        elif c >= '0':
            binStr += bin(ord(c) + 4)[2:].zfill(6)
        # +
        elif c == '+':
            binStr += bin(ord(c) + 19)[2:].zfill(6)
        # /
        else:
            binStr += bin(ord(c) + 16)[2:].zfill(6)
    
    # get rid of the extra 0s created by padding
    if padding > 0:
        extra = len(binStr) % 4
        if extra > 0:
            binStr = binStr[:-extra]
        
        if padding == 2:
            binStr = binStr[: -4]   
            
    # bin -> hex
    return hex(int(binStr, 2))[2:]




# ------------------------------------------------------------------
# Testing
    
b64ToHex('3q2+7w==')            # 'deadbeef'
b64ToHex('oT1C')                # 'a13d42'
b64ToHex('5FI=')                # 'e452'
b64ToHex('Tg==')                # '4e'
