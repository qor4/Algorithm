def solution(name):
    answer = 0
    if name[1] == 'A':
        answer -= 1
    for i in name:
        if ord(i) - ord('A') > (ord('Z') + 1) - ord(i):
            answer += (ord('Z') + 1) - ord(i)
        else:
            answer += ord(i) - ord('A')
        answer += 1
    answer -= 1
    return answer
