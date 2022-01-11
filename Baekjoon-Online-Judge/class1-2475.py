import sys

data = list(map(int, sys.stdin.readline().strip().split()))
num = 0
for i in data:
    num += i ** 2

print(num%10)