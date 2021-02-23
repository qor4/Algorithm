num = int(input())
count = 0

for i in range(num):
    alpha = [0 for i in range(26)]
    str = input()
    word = str[0]
    for j in range(1, len(str)):
        if str[j] != word:
            alpha[ord(word) - 97] += 1
            word = str[j]
        if j == len(str) - 1:
            alpha[ord(str[j]) - 97] += 1

    if max(alpha) <= 1:
        count += 1

print(count)
