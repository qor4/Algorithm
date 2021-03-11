m, n = map(int, input().split())
num_set = [0 for i in range(1000001)]

num_set[1] = 1
for i in range(2, 1000001):
    j = 2
    while(i * j < 1000001):
        num_set[j*i] = 1
        j += 1


for i in range(m, n + 1):
    if num_set[i] != 1:
        print(i)
