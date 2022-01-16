import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))

numbers = list(combinations(card, 3))

cards = 0
for i in numbers:
    temp = sum(i)
    if temp <= m:
        if temp > cards:
            cards = temp
print(cards)

