N = int(input())
score = list(map(float, input().split()))
score_gap = []

sum = 0.0
for i in score:
    sum += i

sum = sum / N
if sum - int(sum) >= 0.5:
    avg = int(sum) + 1

else:
    avg = int(sum)

for i in range(0, N):
    score_gap.append(score[i] - avg)

min = score_gap[0]
num = 0

for i in range(1, N):
    if abs(min) > abs(score_gap[i]):
        min = score_gap[i]
        num = i
    elif abs(min) == abs(score_gap[i]):
        if min < score_gap[i]:
            min = score_gap[i]
            num = i


print(avg, num + 1)