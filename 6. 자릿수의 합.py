n = int(input())
num = list(map(str, input().split()))
result = []

for i in range(len(num)):
    sum = 0
    for j in range(len(num[i])):
        sum += int(num[i][j])
    result.append(sum)

max = 0
index = 0

for i in range(len(result)):
    if max < result[i]:
        max = result[i]

for i in range(len(result)):
    if max == result[i]:
        print(num[i])
        break
