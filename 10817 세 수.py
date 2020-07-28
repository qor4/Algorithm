number = list(map(int, input().split()))

for i in range(0, len(number) - 1):
    for j in range(i + 1, len(number)):
        if number[i] > number[j]:
            temp = number[i]
            number[i] = number[j]
            number[j] = temp

print(number[1])