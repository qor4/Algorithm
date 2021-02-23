n, k = map(int, input().split())

num_list=list(map(int, input().split()))
sum_list = []

count = 1

for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        for m in range(j + 1, len(num_list)):
            sum_list.append(num_list[i]+num_list[j]+num_list[m])

sum_list.sort(reverse=True)

max = sum_list[0]

for i in range(1, len(sum_list)):
    if max > sum_list[i]:
        max = sum_list[i]
        count += 1

    if count == k:
        break
print(max)
