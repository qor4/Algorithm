def solution(answers):
    answer = []
    student = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4 ,2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    count = [0, 0, 0]
    for i in range(len(student)):
        for j in range(len(answers)):
            if answers[j] == student[i][j % len(student[i])]:
                count[i] += 1
    for i in range(len(count)):
        if max(count) == count[i]:
            answer.append(i+1)
    return answer
