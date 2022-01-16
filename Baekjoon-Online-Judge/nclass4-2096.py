import sys
input = sys.stdin.readline

n = int(input())
max_li = [[-1, -1, -1] for i in range(n)]
min_li = [[9*n, 9*n, 9*n] for i in range(n)]
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))
max_li = li.copy()
min_li = li.copy()

for i in range(1, n):


print(li)
print(max_li)
print(min_li)