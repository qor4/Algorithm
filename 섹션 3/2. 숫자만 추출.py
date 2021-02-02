str = input()
num = []
number = 0
count = 0

for i in range(len(str)):
    if str[i].isdigit() == True:
        num.append(str[i])

for i in range(len(num) - 1, -1, -1):
    number += int(num[i]) * (10**(len(num)-i-1))

for i in range(1, number+1):
    if number % i == 0:
        count += 1


print(number)
print(count)


