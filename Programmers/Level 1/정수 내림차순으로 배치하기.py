def solution(n):
    n = sorted([i for i in str(n)], reverse=True)
    answer = int(''.join(n))
    return answer
