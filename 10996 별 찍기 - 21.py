a = int(input())
num = 0
for i in range(0, a):
    for s_1 in range(1, a + 1):
        if ((s_1 % 2) != 0):
            print("*", end = "")
        else:
            print(" ", end = "")
    print("")
    for s_2 in range(1, a + 1):
        if ((s_2 % 2) == 0):
            print("*", end = "")
        else:
            print(" ", end = "")
    if i != a - 1:
        print("")
