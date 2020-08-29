num_1, num_2 = map(list, input().split())
def reserve(num):
    rnum = int(num[2]) * 100
    rnum += int(num[1]) * 10
    rnum += int(num[0])
    return rnum
rnum_1 = reserve(num_1)
rnum_2 = reserve(num_2)

if rnum_1 > rnum_2:
    print(rnum_1)
else:
    print(rnum_2)
