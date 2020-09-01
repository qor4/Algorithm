alphabet = []
str = input()
count = 0
max = 0

for i in range(0, 26):
    alphabet.append(0)

for i in range(len(str)):
    index = ord(str[i].upper()) - 65
    alphabet[index] += 1

max = alphabet[0]
max_index = 0
for i in range(1, 26):
    if max < alphabet[i]:
        max = alphabet[i]
        max_index = i

for i in range(0, 26):
    if alphabet[i] == max:
        count += 1

if count > 1:
    print("?")
else:
    print(chr(max_index + 65), end = "")