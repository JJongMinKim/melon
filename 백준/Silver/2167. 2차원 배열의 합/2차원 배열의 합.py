N, M = map(int, input().split())

numbers = [list(map(int, input().split())) for _ in range(N)]
sums = [([0]*(M+1)) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        sums[i+1][j+1] = sums[i][j+1]+sums[i+1][j]+numbers[i][j]-sums[i][j]

k = int(input())

for _ in range(k):
    i,j,x,y = map(int, input().split())
    
    print(sums[x][y] - sums[i-1][y] - sums[x][j-1] + sums[i-1][j-1])