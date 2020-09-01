n = int(input())
grade = list(map(int, input().split()))
max = grade[0]
max_i = 0
sum = 0
for i in range(1, n):
    if max < grade[i]:
        max = grade[i]
        max_i = i

for j in range(0, n):
    grade[j] = grade[j] / max * 100
    sum += grade[j]

print(sum / n)