comp = []
index = 0
s = input()

for i in range(0, 26):
    comp.append(-1)

for i in range(len(s)):
    if comp[ord(s[i]) - 97] == -1:
        comp[ord(s[i]) - 97] = i

for i in range(len(comp)):
    print(comp[i], end = "")
    if i < len(comp) - 1:
        print(" ", end = "")
