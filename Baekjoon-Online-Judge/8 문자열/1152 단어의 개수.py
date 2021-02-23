str = list(input())
str.append(' ')
count = 0
for i in range(len(str)):
    if str[i] == ' ':
        if str[i - 1] != " ":
            count += 1
print(count)