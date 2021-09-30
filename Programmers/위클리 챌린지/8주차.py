def solution(sizes):
    min_ = -1
    max_ = -1
    for i in sizes:
        if min(i) > min_:
            min_ = min(i)
        if max(i) > max_:
            max_ = max(i) 
    answer = min_ * max_
    return answer
