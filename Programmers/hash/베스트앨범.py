import operator
def solution(genres, plays):
    genre = list(set(genres))
    answer = []
    li = {}
    temp = {}
    for i in genre:
        li[i] = []
        temp[i] = []
    
    for gen, play, idx in zip(genres, plays, range(len(genres))):
        li[gen].append([play, idx])
        temp[gen].append(play)

    temp = list(temp.items())
    temp.sort(key=lambda x:-sum(x[1]))

    for i in li:
        li[i].sort(key=lambda x:-x[0])

    for i in temp:
        for j in li[i[0]][:2]:
            answer.append(j[1])
            print(j)
    
    return answer
