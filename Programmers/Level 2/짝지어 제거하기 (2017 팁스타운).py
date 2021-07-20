#정답 코드
def solution(s):
    answer = -1
    s = list(s)
    stack = []
    for i in s:
        stack.append(i)
        if len(stack) > 1 and stack[len(stack)-1] == stack[len(stack)-2]:
            stack.pop()
            stack.pop()
            
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    return answer
 
#오답 코드
  def solution(s):
    answer = 1
    s = list(s)
    for i in range(len(s)):
        if s.count(s[i]) % 2 != 0:
            return 0
    if len(s) % 2 == 1:
        return 0
    while(len(s) > 0):
        for i in range(len(s)-1):
            if s[i] == s[i + 1]:
                del s[i:i+2]
                break
        else:
            return 0
    return answer
  
  '''
  오답코드 -> 시간 초과, 반복문을 없애고 stack을 사용하여 문제 해결
  '''
