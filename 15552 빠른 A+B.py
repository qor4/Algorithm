import sys
t = int(sys.stdin.readline())

a, b = map(int, sys.stdin.readline().split())
list_a = [a]
list_b = [b]
for i in range(0, t - 1):
    a, b = map(int, sys.stdin.readline().split())
    list_a.append(a)
    list_b.append(b)

for i in range(0, t):
    print(list_a[i] + list_b[i])


