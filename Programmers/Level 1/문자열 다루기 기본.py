def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        return False
    
    for i in s:
        if not i.isdigit():
            return False
    return answer
  
'''
try:
    int(s)
except:
    return False
    
return s.isdigit() and len(s) in (4, 6)
'''
