#1
# n, m = map(int, input().split())
# num = list(map(int, input().split()))
#
# for i in range(n):
#     for j in range(n-1, i, -1):
#         if num[j] < num[j-1]:
#             temp = num[j-1]
#             num[j-1] = num[j]
#             num[j] = temp
#
# for i in range(n):
#     if m == num[i]:
#         print(i+1)


#2
#
# n, m = map(int, input().split())
# num = list(map(int, input().split()))
#
# for i in range(n):
#     for j in range(n-1, i, -1):
#         if num[j] < num[j-1]:
#             temp = num[j-1]
#             num[j-1] = num[j]
#             num[j] = temp
#         if j == i + 1 and num[j - 1] == m:
#             print(j)
#             break

#3
# n, m = map(int, input().split())
# num = list(map(int, input().split()))
#
# for i in range(n):
#     for j in range(n-1, i, -1):
#         if num[j] < num[j-1]:
#             temp = num[j-1]
#             num[j-1] = num[j]
#             num[j] = temp
#         if j == i + 1 and num[j - 1] == m:
#             print(j)
#             exit()

#4
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
for i in range(n):
    if m == num[i]:
        print(i+1)
        break