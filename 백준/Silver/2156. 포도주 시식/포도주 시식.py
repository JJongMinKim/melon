"""
3잔 연속 불가

i일 때
dp[i-3] + arr[i-1] + arr[i]
dp[i-2] + arr[i] 
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
    
if N <= 2:
    print(sum(arr))
    exit()
    
dp = [0]*N
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[2]+arr[1], arr[2]+arr[0], dp[1])

for i in range(3, N):
    dp[i] = max(dp[i-2]+arr[i], dp[i-3] + arr[i-1]+arr[i], dp[i-1])
    
print(dp[N-1])