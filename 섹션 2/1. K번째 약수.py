N, M = map(int, input().split())

count = 0
result = -1

for i in range(1, N + 1):
    if (N % i) == 0:
        count += 1
    if count == M:
        print(i)
        result = 1
        break

else:
    print(result)

