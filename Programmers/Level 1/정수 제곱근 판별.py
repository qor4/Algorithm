import math
def solution(n):
    sqrt = math.sqrt(n) 
    if sqrt - int(sqrt) == 0:
        return (sqrt + 1) * (sqrt + 1)
    else:
        return -1
      
  '''
  sqrt = n ** (1/2)
  파이썬에서 **는 제곱근!!
  '''
