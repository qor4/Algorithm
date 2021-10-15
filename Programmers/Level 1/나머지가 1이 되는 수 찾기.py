def solution(n):
    div = 2
    while True:
        if n % div == 1:
            return div
        else:
            div += 1
