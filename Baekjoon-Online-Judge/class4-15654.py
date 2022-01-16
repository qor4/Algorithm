import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
li = list(permutations(num, m))
li.sort()

for i in li:
    for j in i:
        print(j, end=' ')
    print()
