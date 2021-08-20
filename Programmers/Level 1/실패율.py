def solution(N, stages):
    stage = [stages.count(i) for i in range(1, N + 1)]
    tuple_stage = []
    summ = 0
    for i in range(N):
        if (len(stages) - summ) == 0:
            tuple_stage.append((0, i + 1))
        else:
            tuple_stage.append((stage[i] / (len(stages) - summ), i + 1))
        summ += stage[i]
        
    tuple_stage.sort(key=lambda x:(-x[0], x[1]))
    answer = [i[1] for i in tuple_stage]
    return answer
