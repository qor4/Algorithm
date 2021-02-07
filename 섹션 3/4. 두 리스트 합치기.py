n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

sum_list = n_list + m_list
sum_list.sort()

for i in range(len(sum_list)):
    print(sum_list[i], end= " ")