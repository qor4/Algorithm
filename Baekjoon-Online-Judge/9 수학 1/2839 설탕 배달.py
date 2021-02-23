sugar = int(input())
number = -1
for i in range(0, (sugar // 5) + 1):
    if (sugar - 5 * i) % 3 == 0:
        number = i

if number < 0:
    print(-1)
else:
    print(number + ((sugar - 5 * number) // 3))