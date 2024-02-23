T = int(input())

def isValid(string, stt, end):
    if stt >= end:
        return True
    
    l = stt
    r = end
    
    while l < r:
        if string[l] == string[r]:
            return False
        
        l += 1
        r -= 1
    
    return isValid(string, stt, r-1)

for _ in range(T):
    shapes = input()
    
    if isValid(shapes, 0, len(shapes)-1):
        print('YES')
    else:
        print('NO')