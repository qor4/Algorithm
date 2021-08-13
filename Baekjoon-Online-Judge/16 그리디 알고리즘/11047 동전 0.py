n, k = map(int, input().split())
money = []
count = 0

for i in range(n):
  money.append(int(input()))

idx = len(money) - 1

while k > 0:
  if (k // money[idx]) >= 1:
    count += (k // money[idx])
    k %= money[idx] 
  idx -= 1

print(count)
