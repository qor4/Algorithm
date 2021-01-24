n, m = map(int, input().split())

num = [0 for i in range(n + m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        num[i + j] += 1

max = 0

for i in range(len(num)):
    if num[i] > max:
        max = num[i]

for i in range(len(num)):
    if max == num[i]:
        print(i, end = " ")