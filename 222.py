def path(s):
    if s[0] == "/":
        s = s[1:]
    if s[-1] == "/":
        s = s[:-1]
        
    stack = s.split("/")
    
    i=0
    while i < len(stack):
        if stack[i] == ".":
            del stack[i]
            continue
        elif stack[i] == "..":
            del stack[i]
            if i!=0:
                del stack[i-1]
                i-=1
            continue
        i+=1
    
    return "/" + '/'.join(stack) + "/"
    
    
s= "/../../usr/bin/../bin/./scripts/../"
print(path(s))
