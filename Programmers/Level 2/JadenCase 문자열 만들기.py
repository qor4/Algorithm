def solution(s):
    answer = ''
    s = list(map(str, s.split(" ")))
    string = []

    for i in s:
        if not i == '':
            i = i.lower()
            i = i.replace(i[0], i[0].upper(), 1)
        string.append(i)
        
    answer = " ".join(string)
    return answer
  
  '''
  capitalize() 함수 : 주어진 문자열에서 맨 첫 글자를 대문자로 변환시킨다.
  '''
