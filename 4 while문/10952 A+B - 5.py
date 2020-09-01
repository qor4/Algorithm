result = 1
num = 0
a, b = map(int, input().split())
list_a = [a]
list_b = [b]
while result != 0:
    a, b = map(int, input().split())
    list_a.append(a)
    list_b.append(b)
    result = a + b
    num = num + 1

for i in range(0, num):
    print(list_a[i] + list_b[i])
