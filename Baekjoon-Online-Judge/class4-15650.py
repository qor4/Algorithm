import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

li = list(combinations([i for i in range(1, n+1)], m))
li.sort()

for i in li:
    for j in i:
        print(j, end=' ')
    print()
