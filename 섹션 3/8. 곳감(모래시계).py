n = int(input())
num = []
for i in range(n):
    num.append(list(map(int, input().split())))

m = int(input())

for i in range(m):
    r, d, t = map(int, input().split())
    if d == 0:
        for j in range(t):
            temp = num[r - 1][0]
            for k in range(1, n):
                num[r - 1][k - 1] = num[r - 1][k]
            num[r - 1][n - 1] = temp
    else:
        for j in range(t):
            temp = num[r - 1][n-1]
            for k in range(n-2, -1, -1):
                num[r - 1][k + 1] = num[r - 1][k]
            num[r - 1][0] = temp

start = 0
finish = n
sum = 0
for i in range(n):
    for j in range(start, finish):
        sum += num[i][j]
    if n//2 <= i:
        start -= 1
        finish += 1
    else:
        start += 1
        finish -= 1

print(sum)
