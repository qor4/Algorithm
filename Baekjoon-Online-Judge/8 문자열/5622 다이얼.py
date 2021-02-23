str = input()
time = 0
dial = [[],[],['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
for i in range(len(str)):
    for j in range(len(dial)):
        for k in range(len(dial[j])):
            if str[i] == dial[j][k]:
                time += j + 1

print(time)

