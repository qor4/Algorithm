a = []
for i in range(0, 9):
    a.append(int(input()))

max = a[0]
max_i = 0
for j in range(1, 9):
    if max < a[j]:
        max = a[j]
        max_i = j

print(max)
print(max_i + 1, end = "")