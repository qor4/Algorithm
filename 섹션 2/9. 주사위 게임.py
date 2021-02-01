n = int(input())

reward = []
for i in range(n):
    num_list = list(map(int, input().split()))
    count = 1
    num_list.sort()
    equal = num_list[0]
    for j in range(1, len(num_list)):
        if num_list[j] == equal:
            count += 1
        else:
            if count == 1 :
                equal = num_list[j]
    if count == 1:
        reward.append(equal*100)
    elif count == 2:
        reward.append(1000+(equal*100))
    elif count == 3:
        reward.append(10000+(equal*1000))

reward.sort()
last = len(reward) - 1

print(reward[last])


