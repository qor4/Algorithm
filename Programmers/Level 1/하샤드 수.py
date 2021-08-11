def solution(x):
    answer = True if x % sum([int(i) for i in list(str(x))]) == 0 else False
    return answer
  
  '''
  return n % sum([int(c) for c in str(n)]) == 0
  str(x)해서 굳이 list형으로 안 바꿔줘도 된다.
  그리고 삼항연산자와 return 쓰려면 return 식 if 식 else 식
  -> return True if x % sum([int(i) for i in str(x)]) == 0 else False
  이고, == 0 의 return이 boolean이니까 true false 빼도 됨
  '''
