import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    commands = input().strip()
    N = int(input())
    statement = input().strip()
    statement = statement[1:len(statement)-1]
    arr = []
    if statement:
      arr = deque(list(map(int, statement.split(','))))
    direction = 1
    for i in range(len(commands)):
        if commands[i] == 'R':
            direction *= -1
        else:
            if len(arr) == 0:
                print('error')
                break
            if direction == 1:
                arr.popleft()
            else:
                arr.pop()
    else:
        arr = list(arr)
         
        if direction == -1:
            arr = arr[::-1]
        print('[',end='')
        print(*arr, sep=',',end=']\n')