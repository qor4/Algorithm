n, m = map(int, input().split())

sum = 0
song = list(map(int, input().split()))
for i in song:
    sum += i

lt = sum // m
rt = sum
res = 0
while(lt <= rt):
    mid = (lt + rt) // 2
    mid_tmp = mid
    count = 0
    for i in song:
        if mid_tmp - i > 0:
            mid_tmp -= i
        else:
            mid_tmp = mid
            mid_tmp -= i
            count += 1
    if count >= m:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)