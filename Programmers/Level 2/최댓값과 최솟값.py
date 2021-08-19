def solution(s):
    s = [int(i) for i in list(s.split(' '))]
    answer = str(min(s)) + ' ' + str(max(s))
    return answer
