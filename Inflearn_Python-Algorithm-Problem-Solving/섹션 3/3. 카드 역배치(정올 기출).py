card = [i for i in range(0, 21)]

for i in range(10):
    ai, bi = map(int, input().split())
    for j in range(ai, ai + (((bi - ai) // 2) + 1)):
        temp = card[bi - (j - ai)]
        card[bi - (j - ai)] = card[j]
        card[j] = temp

for i in range(1, 21):
    print(card[i], end=" ")

