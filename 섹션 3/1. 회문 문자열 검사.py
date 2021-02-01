n = int(input())
word_list = []

for i in range(n):
    word_list.append(input())

for i in range(n):
    for j in range(0, len(word_list[i])//2):
        if word_list[i][j].lower() != word_list[i][len(word_list[i])-j-1].lower():
            print("#", (i+1), " NO", sep="")
            break
    else:
        print("#", (i+1), " YES", sep="")