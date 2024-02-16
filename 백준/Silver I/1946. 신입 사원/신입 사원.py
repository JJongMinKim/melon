T = int(input())

for _ in range(T):
    N = int(input())
    
    newbie = []
    for _ in range(N):
        newbie.append(tuple(map(int, input().split())))
        
    newbie.sort()
    
    miv = newbie[0][1]
    cnt = 1
    for i in range(1, len(newbie)):
        if newbie[i][1] < miv:
            cnt +=1
            miv = newbie[i][1]
    print(cnt)