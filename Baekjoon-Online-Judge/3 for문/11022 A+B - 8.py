t = int(input())

a, b = map(int, input().split())
list_a = [a]
list_b = [b]
for i in range (0, t - 1):
    a, b = map(int, input().split())
    list_a.append(a)
    list_b.append(b)

for i in range (0, t):
    print("Case #", i + 1, ": ", list_a[i], " + ", list_b[i], " = ", list_a[i] + list_b[i], sep="")