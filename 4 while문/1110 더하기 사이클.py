a = input()
if int(a) < 10:
    a = "0" + a
result = [a[0], a[1]]
t = 0

while True:
    t = t + 1
    num = str(int(result[0]) + int(result[1]))
    if int(num) < 10:
        num = "0" + num
    result[0] = result[1]
    result[1] = num[1]
    if result[0] == a[0] and result[1] == a[1]:
        break

print(t)
