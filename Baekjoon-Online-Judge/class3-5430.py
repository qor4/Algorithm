import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input())
    x = input().strip()
    x = x[1:-1]
    idx = 1
    if n > 0:
        x = list(map(int, x.split(',')))
        x = deque(x)
    for i in p:
        if i == 'R':
            if len(x) > 0:
                idx *= -1

        elif i == 'D':
            if len(x) > 0:
                if idx == 1:
                    x.popleft()
                else:
                    x.pop()
            else:
                print('error')
                break
    else:
        print('[', end='')
        if idx == 1:
            for i in range(len(x)):
                print(x[i], end='')
                if i != (len(x) - 1):
                    print(',', end='')
        else:
            for i in range(len(x)-1, -1, -1):
                print(x[i], end='')
                if i != 0:
                    print(',', end='')
        print(']')