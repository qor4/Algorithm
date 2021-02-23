num = []
check_list = [0]*9
state = 1
for i in range(9):
    num.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        check_list[num[i][j]-1] = 1
    for j in range(9):
        if check_list[j] == 0:
            state = 0
            break
    check_list = [0] * 9

for i in range(9):
    for j in range(9):
        check_list[num[j][i]-1] = 1
    for j in range(9):
        if check_list[j] == 0:
            state = 0
            break
    check_list = [0] * 9

row, col = 0, 0
for l in range(3):
    for i in range(3):
        for j in range(row, 3 + row):
            for k in range(col, 3 + col):
                check_list[num[j][k] - 1] = 1
        for j in range(9):
            if check_list[j] == 0:
                state = 0
                break
        check_list = [0] * 9
        if (col + 3) > 6:
            col = 0
        col += 3
    row += 3

if state==0:
    print("NO")
else:
    print("YES")