# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 22:59:46 2021

@author: Alfredo
"""

# Daily Coding Problem #431

# Problem:
# Create a basic sentence checker that takes in a stream of characters and 
# determines whether they form valid sentences. If a sentence is valid, 
# the program should print it out.
# We can consider a sentence valid if it conforms to the following rules:
# 1. The sentence must start with a capital letter, followed by a lowercase
#    letter or a space.
# 2. All other characters must be lowercase letters, separators (,,;,:) or
#    terminal marks (.,?,!,‽).
# 3. There must be a single space between each word.
# 4. The sentence must end with a terminal mark immediately following a word.



def isWord(word, separators, terminals):
    # There must be a single space between each word.
    if word == '':
        return False
    
    # All other characters must be lowercase letters, separators (,,;,:) or
    # terminal marks (.,?,!,‽).
    for c in word:
        if not ((c.isalpha() and c.islower()) or c in separators or c in terminals):
            return False
          
    return True
    

def isValid(sentence):
    if len(sentence) < 2:
        return
    
    # The sentence must start with a capital letter, followed by a lowercase
    # letter or a space.
    if not (sentence[0].isupper() and ((sentence[1].isalpha() and sentence[1].islower()) or sentence[1] == ' ')):
        return
    
    separators = {',', ';', ':'}
    terminals = {'.', '?', '!', '‽'}
    arr = sentence.split(' ')
    arr.pop(0)
    
    for word in arr:
        if not isWord(word, separators, terminals):
            return
    
    # The sentence must end with a terminal mark immediately following a word.
    if sentence[-1] not in terminals or sentence[-2] == ' ':
        return
    
    print(sentence)


# -----------------------------------------------------------------------------
# Testing
    
isValid("Hello, World!")        # 
isValid("Hello, world!")        # "Hello, world!"
isValid("Is this a test?")      # "Is this a test?"
isValid("this is a test!")      # 
isValid("This is  a test!")     # 
isValid("This is #a test!")     # 
isValid("A.")                   # 
isValid("Amen.")                # "Amen."
