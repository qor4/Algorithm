n = int(input())
num = []
for i in range(n):
    num.append(list(map(int, input().split())))
max = 0
for i in range(n):
    sum = 0
    for j in range(n):
        sum += num[i][j]
    if max < sum:
        max = sum

for i in range(n):
    sum = 0
    for j in range(n):
        sum += num[j][i]
    if max < sum:
        max = sum

sum = 0
for i in range(n):
    sum += num[i][i]
    if max < sum:
        max = sum

sum = 0
for i in range(n - 1, -1, -1):
    sum += num[i][i]
    if max < sum:
        max = sum

print(max)