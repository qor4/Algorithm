def solution(progresses, speeds):
    count = 0
    answer = []
    for i in range(len(progresses)):
        tmp = (100 - progresses[i]) // speeds[i]
        if ((100 - progresses[i]) % speeds[i]) != 0:
            tmp = tmp + 1
        progresses[i] = tmp
    
    tmp = progresses[0]
    for i in range(len(progresses) - 1):
        if tmp >= progresses[i+1]:
            count = count + 1
        else:
            answer.append(count+1)
            count = 0
            tmp = progresses[i+1]
    answer.append(count+1)
    return answer
