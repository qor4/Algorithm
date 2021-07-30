def solution(arr):
    answer = []
    sort_arr = arr.copy()
    sort_arr.sort()
    arr.remove(sort_arr[0])
    if len(arr) == 0:
        return [-1]
    answer = arr.copy()
    return answer
  
  '''
  답은 맞지만 가장 작은 수가 여러개 있을 때 그 중 하나만 지워짐.
  
  다른 사람 풀이
  def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]
  '''
