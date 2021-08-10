def solution(scores):
    answer = ''
    scores_tmp = []
    scores_tmp2 = []
    score = []
    for i in range(len(scores)):
        for j in range(len(scores)):
            scores_tmp.append(scores[j][i])
        scores_tmp2.append(scores_tmp)
        scores_tmp = []
    for i in range(len(scores)):
        if min(scores_tmp2[i]) == scores_tmp2[i][i] or max(scores_tmp2[i]) == scores_tmp2[i][i]:
            if scores_tmp2[i].count(scores_tmp2[i][i]) > 1:
                score.append(sum(scores_tmp2[i]) / len(scores_tmp2[i]))
            else:
                score.append((sum(scores_tmp2[i]) - scores_tmp2[i][i]) / (len(scores_tmp2[i]) - 1))
        else:
            score.append(sum(scores_tmp2[i]) / len(scores_tmp2[i]))
    for i in score:
        if i >= 90:
            answer += 'A'
        elif i >= 80:
            answer += 'B'         
        elif i >= 70:
            answer += 'C' 
        elif i >= 50:
            answer += 'D'  
        else:
            answer += 'F'  
    return answer
