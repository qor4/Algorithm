t = int(input())
list_t = []
for i in range(t):
    list_t.append(list(map(int, input().split())))
for i in range(t):
    if list_t[i][0] >= list_t[i][2]:
        print((list_t[i][2]) * 100 + 1)
    else:
        if list_t[i][2] % list_t[i][0] == 0:
            ans = (list_t[i][0] * 100) + list_t[i][2] // list_t[i][0]
        else:
            ans = (list_t[i][2] % list_t[i][0]) * 100 + (list_t[i][2] // list_t[i][0] + 1)
        print(int(ans))
