N = int(input())

count = 0
num_list = [0] * (N + 1)


for i in range(2, N + 1):
    if num_list[i] != 1:
        for j in range(2 * i, N + 1, i):
            num_list[j] = 1
    if num_list[i] == 0:
        count += 1


print(count)
