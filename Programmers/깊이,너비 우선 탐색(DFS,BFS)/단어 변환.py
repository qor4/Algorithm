def solution(begin, target, words):
    answer = 0
    li = [begin]
    
    if target not in words:
        return 0
    
    while target not in li:
        temp = li.copy()
        li = []
        for start in temp:
            for word in words:
                cnt = 0
                for alphabet1, alphaber2 in zip(start, word):
                    if alphabet1 == alphaber2:
                        cnt += 1
                if cnt == len(begin)-1:
                    li.append(word)
        answer += 1
    return answer
