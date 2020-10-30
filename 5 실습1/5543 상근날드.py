menu = []
for i in range(0, 5):
    num = int(input())
    menu.append(num)

if menu[3] < menu[4]:
    min_d = menu[3]
else:
    min_d = menu[4]

min_h = menu[0]
for j in range(1, 3):
    if min_h > menu[j]:
        min_h = menu[j]

print(min_d + min_h - 50)
