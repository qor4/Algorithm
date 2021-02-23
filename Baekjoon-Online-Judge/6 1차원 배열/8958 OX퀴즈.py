n = int(input())
a = []
sum = 0
score = 0
for i in range(n):
    a.append(input())

for j in range(n):
    for k in range(len(a[j])):
        if a[j][k] == "O":
            score += 1
            sum += score
        else:
            score = 0
    a[j] = sum
    score = 0
    sum = 0

for l in range(n):
    print(a[l])