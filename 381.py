# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 13:00:57 2020

@author: Alfredo
"""

# Daily Coding Problem #381

# Problem:
# Implement a function that converts a hex string to base64.

def base64(hexStr):
    b64Str = ''
    
    # hex string -> binary
    binStr = bin(int(hexStr, 16))[2:].zfill(len(hexStr)*4)
    
    # adding zeroes to last triple of bytes
    extra = len(binStr) % 24
    if extra > 0:
        binStr += '0' * (24 - extra)
        
    print(binStr)
    print(extra)
        
    for i in range(0, len(binStr), 6):
        # decimal representation of current b64 character
        curChar = int(binStr[i:i+6], 2)
        
        # A-Z
        if curChar < 26:
            b64Str += chr(curChar + 65)
        # a-z
        elif curChar < 52:
            b64Str += chr(curChar + 71)
        # 0-9
        elif curChar < 62:
            b64Str += chr(curChar - 4)
        # +
        elif curChar == 62:
            b64Str += chr(curChar - 19)
        # /
        else:
            b64Str += chr(curChar - 16)
            
    # adding padding if needed
    if extra == 0 or extra > 16:
        return b64Str
    elif extra < 9:
        return b64Str[:-2] + '=='
    else:
        return b64Str[:-1] + '='

# ------------------------------------------------------------------
# Testing
base64('deadbeef')      # '3q2+7w=='
base64('a13d42')        # 'oT1C'
base64('e452')          # '5FI='
base64('4e')            # 'Tg=='
