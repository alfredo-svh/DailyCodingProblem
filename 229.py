def solver(snakes, ladders, pos, turns):
    if pos >= 94:
        return turns+1
    
    
    if pos in snakes:
        pos = snakes[pos]
    elif pos in ladders:
        pos = ladders[pos]
        
    
    mxDice = pos+1
    mxRes = 0
    for i in range(1,7):
        if pos+i in ladders:
            curRes = ladders[pos+i]
        elif pos+i in snakes:
            curRes = snakes[pos+i]
        else:
            curRes = pos+i
        
        if curRes > mxRes:
            mxDice = pos+i
            mxRes = curRes
    
    return solver(snakes, ladders, mxDice, turns+1)
    
    
    
    
snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
pos = 1
turn = 0
print(solver(snakes, ladders, pos, turn))
