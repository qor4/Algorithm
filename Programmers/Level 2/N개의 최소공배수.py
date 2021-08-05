def least_common_multiple(a, b):
    div = 2
    com_mul = 1
    while (div <= min(a, b)):
        if a % div == 0 and b % div == 0:
            a = a // div
            b = b // div
            com_mul *= div
            div = 2
        else:
            div += 1
    com_mul *= a * b
    return com_mul
            
def solution(arr):
    answer = 1
    a = arr[0]
    for i in range(1, len(arr)):
        b = arr[i]
        a = least_common_multiple(a, b)
        
    answer = a
    return answer
  
''' gcd 함수 사용한 사람 있음'''
