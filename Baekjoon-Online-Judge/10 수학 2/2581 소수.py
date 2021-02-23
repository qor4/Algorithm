M = int(input())
N = int(input())

a = [k for k in range(M, N + 1)]
count = 0
sum = 0
min = -1

for i in range(len(a)):
    if a[i] == 2:
        count += 1
        sum += a[i]
        if count == 1:
            min = a[i]
    for j in range(2, a[i]):
        if a[i] == 1:
            break
        if a[i] % j == 0:
            break
        if j == (a[i] - 1):
            count += 1
            sum += a[i]
            if count == 1:
                min = a[i]

if sum == 0:
    print(min)
else:
    print(sum)
    print(min)