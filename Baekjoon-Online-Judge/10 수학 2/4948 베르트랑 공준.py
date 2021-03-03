print_list = []
while(True):
    n = int(input())
    if n == 0:
        break
    for i in range(n+1, (2*n)+1):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count += 1
    print_list.append(count)

for i in range(len(print_list)):
    print(print_list[i])

