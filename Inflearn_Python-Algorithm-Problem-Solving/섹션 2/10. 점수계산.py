n = int(input())

answer = list(map(int, input().split()))
score = 0
count = 0
for i in range(n):
    if answer[i] == 1:
        count += 1
        score += count
    else:
        count = 0

print(score)