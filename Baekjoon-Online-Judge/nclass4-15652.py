# import sys
# from itertools import permutations
#
# n, m = map(int, sys.stdin.readline().split())
#
# li = list(permutations([i for i in range(1, n+1)], m))
# for i in range(1, n+1):
#     li.append((i, i))
# li.sort()
#
# for i in li:
#     for j in i:
#         print(j, end=' ')
#     print()
