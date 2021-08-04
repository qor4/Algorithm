def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        if sign == 1:
            answer += absolute
        elif sign == 0:
            answer -= absolute
    
    return answer
