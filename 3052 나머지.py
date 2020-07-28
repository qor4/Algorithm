a = []
for i in range(0, 10):
    a.append(int(input()) % 42)

count = 0
over = 0
for i in range(0, 9):
    for j in range(i + 1, 10):
        if a[i] == a[j]:
            over = 1
    if over == 1:
        count += 1
        over = 0

print(10 - count)
