T = int(input())
sort_list = []

for i in range(T):
    N, s, e, k = map(int, input().split())
    num_list = list(map(int, input().split()))
    for j in range(s - 1, e):
        sort_list.append(num_list[j])
    sort_list.sort()
    print("#" + str(i + 1) + " " + str(sort_list[k - 1]))
    del(num_list[:])
    del(sort_list[:])
