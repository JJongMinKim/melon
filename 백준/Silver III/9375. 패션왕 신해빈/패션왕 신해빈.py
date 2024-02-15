import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    dic = {}
    for _ in range(N):
        item, type = input().split()
        
        if type in dic:
            dic[type].append(item)
        else:
            dic[type] = [item]
    
    answer = 1
    for k in dic.keys():
        answer *= (len(dic[k])+1)
        
    print(answer-1)