a = int(input())
b = int(input())
c = int(input())

cal = str(a * b * c)
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(cal)):
    if cal[i] == "0":
        result[0] += 1
    elif cal[i] == "1":
        result[1] += 1
    elif cal[i] == "2":
        result[2] += 1
    elif cal[i] == "3":
        result[3] += 1
    elif cal[i] == "4":
        result[4] += 1
    elif cal[i] == "5":
        result[5] += 1
    elif cal[i] == "6":
        result[6] += 1
    elif cal[i] == "7":
        result[7] += 1
    elif cal[i] == "8":
        result[8] += 1
    elif cal[i] == "9":
        result[9] += 1

for j in range(0, 10):
    print(result[j])
