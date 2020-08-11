count = 99
seq = 0
comp = 0
count_comp = 0
n = input()
def d(j):
    global seq
    global comp
    global count
    global count_comp
    count_comp = 0
    comp = int(j[0]) - int(j[1])

    for i in range(1, len(j) - 1):
        seq = int(j[i]) - int(j[i + 1])
        if comp == seq:
            count_comp += 1

    if count_comp == len(j) - 2:
        count += 1

if int(n) <= 99:
    print(int(n))
else:
    for j in range(100, int(n) + 1):
        d(str(j))
    print(count)

