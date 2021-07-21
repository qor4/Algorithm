def solution(lottos, win_nums):
    answer = []
    win_count = 0
    zero_count = lottos.count(0)
    for i in win_nums:
        if i in lottos:
            win_count += 1
    high_rank = 7 - (win_count + zero_count)
    low_rank = 7 - win_count
    if low_rank == 7:
        low_rank = 6
    if high_rank == 7:
        high_rank = 6
    answer = [high_rank, low_rank]
    return answer
