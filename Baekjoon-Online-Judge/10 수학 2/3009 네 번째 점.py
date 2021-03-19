x_num=[]
y_num=[]
for i in range(3):
    x, y = map(int, input().split())
    x_num.append(x)
    y_num.append(y)

for i in range(len(x_num)):
    if x_num.count(x_num[i]) % 2 != 0:
        print(x_num[i], end=" ")

for i in range(len(y_num)):
    if y_num.count(y_num[i]) % 2 != 0:
        print(y_num[i])