'''
Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same.
If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
'''


import collections


def rearr(s):
    res = ""
    c = collections.Counter(s)
    
    
    if c.most_common(1)[0][1] > (len(s)//2) + 1:
        return None
    
    while (1):
        done = True
        for char, cnt  in c.most_common():
            if cnt != 0:
                res +=char
                c[char] -= 1
                done = False
        
        if done == True:
            break
    
    return res
    

s = "aaaacccbbb"
print(rearr(s))
