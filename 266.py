# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:39:12 2020

@author: Alfredo
"""


# Daily Coding Problem #266

# Problem:
# A step word is formed by taking a given word, adding a letter, and 
# anagramming the result. For example, starting with the word "APPLE", 
# you can add an "A" and anagram to get "APPEAL".
# Given a dictionary of words and an input word, create a function that
# returns all valid step words.


def step(words, inWord):
    inChars = {}
    stepWords = []
    
    # fill char count of input word
    for c in inWord:
        if c not in inChars:
            inChars[c] = 1
        else:
            inChars[c] +=1
    
    
    # for each word in the word dictionary,
    # we compare its char count with that of our input word
    # if there is only an extra letter in the word, the word is added
    # to our step words
    for word in words:
        cmp = inChars.copy()
        extraLetters = 0
        for c in word:
            if c not in cmp:
                extraLetters+=1
            else:
                if cmp[c] > 1:
                    cmp[c]-=1
                else:
                    del cmp[c]
            

            if extraLetters > 1:
                break
        
        if len(cmp) == 0 and extraLetters == 1:
            stepWords.append(word)
    
    return stepWords
            
            
# Testing
inword = "APPLE"

words = ['APPEAL']
step(words, inword)     # ['APPEAL']

words = ["APPEAL", "APPLICT"]
step(words, inword)     # ['APPEAL']

words = ["APPEAL", "APPLICT", "APPLES"]
step(words, inword)     # ['APPEAL', 'APPLES']
