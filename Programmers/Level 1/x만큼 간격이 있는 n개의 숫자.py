def solution(x, n):
    answer = [0] * n if x == 0 else [i for i in range(x, x * n + ((x * n) // abs(x * n)), x)]
    return answer
