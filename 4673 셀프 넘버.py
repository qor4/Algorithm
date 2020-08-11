list_10000 = [1]
result = 0

def d(n):
    global result
    global list_10000
    result = 0
    if n < 10:
        result = n + n
        if result < 10001:
            list_10000[result] = 1

    else:
        n = str(n)
        for a in range(0, len(n)):
            result += int(n[a])

        result += int(n)
        if result < 10001:
            list_10000[result] = 1


for i in range(10001):
    list_10000.append(0)

for j in range(0, 10001):
    d(j)

for j in range(0, 10001):
    if list_10000[j] == 0:
        print(j)

