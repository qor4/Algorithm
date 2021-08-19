def solution(n):
    answer = ''
    number = {0:'4', 1:'1', 2:'2', 3:'4'}
    while True:
        if n != 0:
            answer = number[n % 3] + answer
        if n // 3 > 0:
            if n % 3 == 0:
                n = (n - 1) // 3
            else:
                n = n // 3
        else:
             break
    return answer
