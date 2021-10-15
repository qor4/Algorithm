import itertools

def solution(numbers):
    comb = list(itertools.combinations(numbers, 2))
    answer = list(set([i[0]+i[1] for i in comb]))
    answer.sort()
    return answer
