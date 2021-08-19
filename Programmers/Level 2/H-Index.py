def solution(citations):
    answer = 0
    count = []
    if citations.count(0) == len(citations):
        return 0
    for i in range(max(citations)):
        if len([a for a in citations if i <= a]) >= i:
            count.append(i)
    return max(count)
