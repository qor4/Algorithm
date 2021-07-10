#정답 코드
import heapq

def solution(operations):
    answer = []
    heap = []
    for op in operations:
        tmp = op.split(" ")
        if tmp[0] == "I":
            heapq.heappush(heap, int(tmp[1]))
        elif tmp[0] == "D":
            if len(heap) > 0:
                if int(tmp[1]) > 0:
                    del heap[len(heap) - 1]
                else:
                    heapq.heappop(heap)
    if len(heap) > 0:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer = [0, 0]
    return answer
  
  #오답 코드
  import heapq

def solution(operations):
    answer = []
    heap = []
    for op in operations:
        tmp = op.split(" ")
        if tmp[0] == "I":
            heapq.heappush(heap, int(tmp[1]))
        elif tmp[0] == "D":
            if len(heap) > 0:
                if int(tmp[1]) > 0:
                    del heap[len(heap) - 1]
                else:
                    heapq.heappop(heap)
    if len(heap) > 0:
        answer.append(heap[len(heap) - 1])
        answer.append(heap[0])
    else:
        answer = [0, 0]
    return answer
  
  '''
  마지막에 heap의 인덱스로 답을 return하면 오답이고 max(), min() 함수를 썼을 때 정답.
  -> 힙 구조는 가장 우선순위가 높은 값이 먼저 pop 되는 것을 보장하는 자료구조로
  0번 인덱스가 가장 우선순위가 높은 값(가장 작은 값)은 맞지만, 나머지 값에 대한 정렬은 보장하지 않음.
  '''
