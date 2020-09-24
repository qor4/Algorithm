T = int(input())
n = list(map(int, input().split()))
count = 0

for i in range(len(n)):
    if n[i] == 2:
        count += 1


    for j in range(2, n[i]):
        if n[i] == 1:
            break
        if n[i] % j == 0:
            break
        if j == (n[i] - 1):
            count += 1

print(count)