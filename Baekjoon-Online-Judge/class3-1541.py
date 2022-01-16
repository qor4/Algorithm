import sys

st = input().strip()

li = []
num = ''
for i in st:
    if i.isdigit():
        num += i
    else:
        li.append(int(num))
        if i == '-':
            li.append(i)
        num = ''
li.append(int(num))

result = []
idx = 1
while idx:
    if '-' in li:
        idx = li.index('-')
        result.append(sum(li[:idx]))
        li = li[idx + 1:]
    else:
        idx = 0

if result:
    re = result[0]
    for i in range(1, len(result)):
        re -= result[i]
    re -= sum(li)
else:
    re = sum(li)
print(re)



