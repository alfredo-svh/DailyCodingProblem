# Problem #260:
#
# The sequence [0, 1, ..., N] has been jumbled, and the only
# clue you have for its order is an array representing whether each
# number is larger or smaller than the last. Given this information,
# reconstruct an array that is consistent with it. For example, given 
# [None, +, +, -, +], you could return [1, 2, 3, 0, 4].


def reconstruct(arr):
    
    plusCount = 0
    
    for i in range(1, len(arr)):
        if arr[i]=='+':
            plusCount+=1
    
    res = [len(arr) - 1 - plusCount]
    
    smaller = res[0] -1
    bigger = res[0] +1
    
    for i in range(1, len(arr)):
        if arr[i] == '+':
            res.append(bigger)
            bigger+=1
        else:
            res.append(smaller)
            smaller -= 1
        
    return res


# Testing
a = [None, '+','+','+']
b = [None, '+', '+', '-', '+']
reconstruct(a)      # [0, 1, 2, 3]
reconstruct(b)      # [1, 2, 3, 0, 4]
