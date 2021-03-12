print_list = []
num_set = [0 for i in range((2*123456) + 1)]
num_set[1] = 1
for i in range(2, (2*123456) + 1):
    j = 2
    while((i * j) < ((2*123456) + 1)):
        num_set[j*i] = 1
        j += 1

while(True):
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n+1, (2*n)+1):
        if num_set[i] != 1:
            count += 1
    print_list.append(count)

for i in range(len(print_list)):
    print(print_list[i])

