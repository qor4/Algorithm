t = int(input())
list_t = []
list_v = []
ans = []

def sum(k, n):

    global list_v
    sum = 0
    for i in range(1, n + 1):
        sum += list_v[k - 1][i]

    return sum

#입력 받음
for i in range(t):
    list_t.append([])
    for j in range(2):
        list_t[i].append(int(input()))

for m in range(t):
    k = list_t[m][0]
    n = list_t[m][1]
    list_v.clear() #행, 열 모두 사라짐(2차원 배열 -> [])
    for l in range(k + 1):
        list_v.append([])
        for m in range(n + 1):
            if l == 0:
                list_v[0].append(m)
            elif m == 0:
                list_v[l].append(0)
            else:
                list_v[l].append(sum(l, m))
    ans.append(list_v[k][n])

for m in range(t):
    print(ans[m])

