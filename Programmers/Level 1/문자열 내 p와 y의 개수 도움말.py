def solution(s):
    answer = True
    s = s.lower()
    if s.count('p') == s.count('y'):
        return True
    else:
        return False
