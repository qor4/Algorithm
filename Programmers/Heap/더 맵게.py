#정답 코드
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(any(K > sc for sc in scoville)):
        if len(scoville) <= 1:
            return -1
        tmp = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, tmp)
        answer += 1
    return answer
  
#오답 코드  
def solution(scoville, K):
    answer = 0
    scoville.sort()
    while(any(K > sc for sc in scoville)):
        if len(scoville) <= 1:
            return -1
        tmp = scoville[0] + (scoville[1] * 2)
        del scoville[:2]
        scoville.append(tmp)
        scoville.sort()
        answer += 1
    return answer
  
  '''
  매번 while문에서 sort 함수를 실행시키다보니 리스트의 길이가 길어질 떄 많은 시간이 소요되어서 효율성 부분에서 시간초과.
  heapq는 push할 때마다 자동으로 정렬해주는 모듈로 속도가 훨씬 빠르다!
  heapq.heapify(list) -> 리스트를 heapq로 바꿔줌
  heapq.heappop(heapq) -> pop 기능
  heapq.heappush(heapq, value) -> push 기능
 '''
  
