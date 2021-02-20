n = int(input())
num = []
count = 0
for i in range(n):
    num.append(list(map(int, input().split())))
num.insert(0, [0]*n)
num.append([0]*n)
for i in range(n+2):
    num[i].insert(0, 0)
    num[i].append(0)

for i in range(1, n+1):
    for j in range(1, n+1):
        if num[i][j] > num[i-1][j] and num[i][j] > num[i][j-1] and num[i][j] > num[i][j+1] and num[i][j] > num[i+1][j]:
            count += 1
print(count)
