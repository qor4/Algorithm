import sys

input = sys.stdin.readline

n, m = map(int, input().split())

names = []
for _ in range(n+m):
    names.append(input().strip())

names = sorted(names)
solved = []
for i in range(1, n+m):
    if names[i] == names[i-1]:
        solved.append(names[i])
print(len(solved))
for i in solved:
    print(i)
