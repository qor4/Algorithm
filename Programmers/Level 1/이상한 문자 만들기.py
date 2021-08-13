def solution(s):
    s = list(s.split(" "))
    for i in range(len(s)):
        tmp = ''
        for j in range(len(s[i])):
            tmp = tmp + s[i][j].upper() if j % 2 == 0 else tmp + s[i][j].lower()
        s[i] = tmp
    answer = ' '.join(s)
    return answer
  
'''
enumerate -> 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환
return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])
'''
