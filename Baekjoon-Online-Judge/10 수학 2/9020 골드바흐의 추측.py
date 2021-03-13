t = int(input())

num_set = [0 for i in range(10001)]
num_set[1] = 1
num_set[0] = 1

for i in range(2, 10001):
    j = 2
    while(i * j < 10001):
        num_set[j*i] = 1
        j += 1

for i in range(t):
    n = int(input())
    index = n // 2
    for i in range(index, 1, -1):
        if num_set[i] == 0 and num_set[n - i] == 0:
            print(i, n - i)
            break
