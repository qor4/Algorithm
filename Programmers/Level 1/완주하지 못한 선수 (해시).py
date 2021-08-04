#정답코드
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    completion.append("0")
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]

#효율성 오답 코드
def solution(participant, completion):
    answer = ''
    for i in participant:
        if i in completion:
            completion.remove(i)
        else:
            return i
    return answer
