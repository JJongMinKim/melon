"""
() => 레이저
(    ) => 쇠막대기
막대기 안에 레이저 개수+1 이 총 토막 개수

스택에 넣고 빼는데 인덱스를 같이 넣어 인덱스 차이가 1이면 레이저
아니면 막대기
"""
import sys
input = sys.stdin.readline
statement = input().strip()

stack = []

answer = 0
for i in range(len(statement)):
    if statement[i] == '(':
        stack.append(i)
    else:
        idx = stack.pop()
        
        if i - idx == 1:
            answer += len(stack)
        else:
            answer += 1
            
print(answer)