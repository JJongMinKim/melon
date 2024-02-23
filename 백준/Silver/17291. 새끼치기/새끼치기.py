"""
1년 2월에 1마리 탄생
매년 1월이 되면 분열
홀수년도에 탄생한 개체는 3번 분열시, 짝수년도에 탄생한 개체는 4번 분열시 사망

N년 말 개체수?
"""

N = int(input())

dp = [0]*21
dp[0] = 1
dp[1] = 1
for y in range(2,N+1):
    dp[y] = dp[y-1]*2
    dp[y] -= dp[y-4] + dp[y-5] if not y % 2 else 0
print(dp[N])