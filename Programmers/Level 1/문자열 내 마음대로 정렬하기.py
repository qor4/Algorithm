def solution(strings, n):
    answer = []
    tmp = []
    for i in strings:
        tmp.append((i[n], i))
    tmp.sort()
    for i in range(len(strings)):
        answer.append(tmp[i][1])
    return answer
