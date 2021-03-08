#1
# k, n = map(int, input().split())
# num = []
# sum = 0
# for i in range(k):
#     num.append(int(input()))
#     sum += num[i]
# div = sum // n
# while(True):
#     sum_n = 0
#     for i in range(k):
#         sum_n += (num[i] // div)
#     if sum_n < n:
#         div -= 1
#     else:
#         print(div)
#         break

#2
k, n = map(int, input().split())
num = []
largest = 0
mid = 0
for i in range(k):
    num.append(int(input()))
    largest = max(largest, num[i])
lt = 0
rt = largest
while lt <= rt:
    mid = (lt+rt) // 2
    count = 0
    for i in num:
        count += i // mid
    if count >= n:
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1

print(res)