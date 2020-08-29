str = input()
count = 0
i = 0
while i < len(str):
    if i + 1 < len(str):
        if str[i] == "c" and (str[i + 1] == "=" or str[i + 1] == "-"):
            i += 1
        elif str[i] == "d" and str[i + 1] == "-":
            i += 1
        elif str[i] == "l" and str[i + 1] == "j":
            i += 1
        elif str[i] == "n" and str[i + 1] == "j":
            i += 1
        elif (str[i] == "z" or str[i] == "s") and str[i + 1] == "=":
            i += 1
        if i + 2 < len(str):
            if str[i] == "d" and (str[i + 1] == "z" and str[i + 2] == "="):
                i += 2

    count += 1
    i += 1

print(count)

