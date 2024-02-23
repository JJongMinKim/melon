N=int(input())
vilage=[[]for _ in range(N)]

po=0
for i in range(N):
    X,A=map(int,input().split())
    vilage[i]=[X,A]
    po+=A
now=0
vilage.sort(key=lambda x:(x[0]))
for i in range(N):
    now+=vilage[i][1]
    if now>=po/2:
        print(vilage[i][0])
        break