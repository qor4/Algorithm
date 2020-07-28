a = int(input())
num = 0
for i in range(1, 2 * a):
    if i == a * 2 - 1:
        num = 1
    if i > a:
        i = 2 * a - i
    for b in range(1, i):
        print(" ", end = "")
    for s in range(1, (2 * a) - 2 * i + 2):
        print("*", end = "")
    if num != 1:
        print("")