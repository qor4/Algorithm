n, m = map(int, input().split())
num_list = list(map(int, input().split()))
count = 0

for i in range(0, n):
    sum = 0
    if num_list[i] <= m:
        for j in range(i, n):
            sum += num_list[j]
            if sum > m:
                break
            elif sum == m:
                count += 1
                break

print(count)
