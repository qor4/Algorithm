n = int(input())
sum = 0
st_num = 0
result = []
for i in range(0, n):
    st = list(map(int, input().split()))
    for j in range(1, st[0] + 1):
        sum += st[j]
    ave = sum / st[0]
    for j in range(1, st[0] + 1):
        if st[j] > ave:
            st_num += 1
    result.append(round(st_num / st[0] * 100, 3))
    st_num = 0
    sum = 0

for j in range(0, len(result)):
    print('%.3f' %result[j], "%", sep = "")