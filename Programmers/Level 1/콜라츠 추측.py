def solution(num):
    answer = 0
    while answer < 501:
        if num == 1:
            return answer
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
            
        answer += 1
        
    return -1
