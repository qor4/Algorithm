def solution(n, lost, reserve):
    answer = 0
    count = 0
    del_lost = []
    del_reserve = []
    for i in lost:
        if i in reserve:
            del_reserve.append(i)
    for i in del_reserve:
        reserve.remove(i)
        lost.remove(i)
    for i in lost:
        if i-1 in reserve:
            del_lost.append(i)
            reserve.remove(i-1)
        elif i+1 in reserve:
            del_lost.append(i)
            reserve.remove(i+1)
    for i in del_lost:
        lost.remove(i)
    answer = n - len(lost)
    return answer
  
  '''
  테스트케이스 13번만 실패
  '''
