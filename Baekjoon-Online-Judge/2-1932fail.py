import sys

n = int(sys.stdin.readline().strip())
triangle = []
for _ in range(n):
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    triangle.append(numbers)
print(triangle)
list = [triangle[0]]
list[0].insert(0, 0)
print(list)

for i in range(n-1):
    temp = []
    while list:
        value = list.pop(0)
        index = value.pop(0)
        print(value)
        print(index)
        num1 = value.copy()
        num2 = value.copy()

        num1.append(triangle[i + 1][index])
        num1.insert(0, index)
        num2.append(triangle[i + 1][index + 1])
        num2.insert(0, index + 1)

        temp.append(num1)
        temp.append(num2)
        print(temp)
    list = temp.copy()
max = 0
for i in list:
    if sum(i[1:])>max:
        max = sum(i[1:])

print(max)
