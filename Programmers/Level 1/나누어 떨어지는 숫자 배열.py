def solution(arr, divisor):
    answer = [i for i in sorted(arr) if i % divisor == 0]
    return answer if len(answer) > 0 else [-1]
