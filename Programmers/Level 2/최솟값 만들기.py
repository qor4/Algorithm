def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse = True)

    for a, b in zip(A, B):
        answer += a * b

    return answer
  
'''
list.sort()는 list 내부에서 정렬되고 None을 반환함
sorted(list)는 기존의 list는 변경되지 않고 정렬된 새로운 list를 반환함.
'''
