# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 12:13:07 2020

@author: Alfredo
"""

# Daily Coding Problem #274

# Problem:
# Given a string consisting of parentheses, single digits, and positive
# and negative signs, convert the string into a mathematical expression
# to obtain the answer.
# Don't use eval or a similar built-in parser.



def evalString(s):
    # stack of operations and stack of numbers
    op = []
    nums = []
    
    #get rid of whitespace
    s = s.replace(' ', '')
    
    i=0
    
    while i < len(s):
        # current character is a digit
        if s[i].isdigit():
            #if number comes after an operation, solve it and insert the
            #result, otherwise simply append the number
            if len(op) == 0 or op[-1]=='(':
                nums.append(int(s[i]))
            else:
                if op[-1] == '-':
                    
                    if len(nums) > 0:
                        nums[-1] = nums[-1] - int(s[i])
                    else:
                        nums.append(- int(s[i]))
                    
                    del op[-1]
                    
                elif op[-1] == '+':
                    nums[-1]+= int(s[i])
                    del op[-1]
                    
                        
        #current character is ')'
        elif s[i] == ')':
            del op[-1]
            #if the parenthesis is preceded by an operation, we use the
            #result of the parenthesis to solve the operation
            if len(op) != 0:
                if op[-1] == '-':
                    if len(nums) > 1:
                        nums[-2] = nums[-2] - nums[-1]
                        del nums[-1]
                    else:
                        nums[-1] = -nums[-1]
                    del op[-1]
                elif op[-1] == '+':
                    nums[-2] = nums[-2] + nums[-1]
                    del nums[-1]
                    del op[-1]
                    

        #current character is '(' or '+' or '-'
        else:
            op.append(s[i])
            
        i+=1
    
    #the nums stack should always end up with a single element,
    #which holds the result 
    return nums[0]



# Testing
s = '-1 + (2 + 3)'
evalString(s)   # 4

s = '4 - ((2 + 3)-2)'
evalString(s)   # 1

s = '1 - ((2 - 3)-2)'
evalString(s)   # 4

s = '1 + ((2 - 3)-2)'
evalString(s)   # -2
