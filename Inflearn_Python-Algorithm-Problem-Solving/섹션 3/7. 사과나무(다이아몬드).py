n = int(input())
num = []
for i in range(n):
    num.append(list(map(int, input().split())))

sum = 0
state = 0
j = 1
for i in range(n):
    start = (n - j) // 2
    for k in range(start, start + j):
        sum += num[i][k]
    if(j == n):
        state = 1
    if(state == 0):
        j += 2
    else:
        j -= 2


print(sum)

