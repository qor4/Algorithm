num = []
check_list = [0]*9
state = 1
for i in range(7):
    num.append(list(map(int, input().split())))

count = 0
for i in range(7):
    for j in range(3):
        if num[i][j]==num[i][j+4] and num[i][j+1]==num[i][j+3]:
            count += 1

for i in range(7):
    for j in range(3):
        if num[j][i]==num[j+4][i] and num[j+1][i]==num[j+3][i]:
            count += 1

print(count)