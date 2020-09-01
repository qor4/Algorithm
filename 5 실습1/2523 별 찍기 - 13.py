a = int(input())
num = 0
for i in range(1, 2 * a):
    if i == a * 2 - 1:
        num = 1
    if i > a:
        i = 2 * a - i
    for j in range(0, i):
        print("*", end = "")
    if num != 1:
        print("")