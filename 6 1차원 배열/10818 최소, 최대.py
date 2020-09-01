c = int(input())
list_c = list(map(int, input().split()))

min = list_c[0]
max = list_c[0]

for i in range(1, c):
    if min > list_c[i]:
        min = list_c[i]
    if max < list_c[i]:
        max = list_c[i]

print(min, max)