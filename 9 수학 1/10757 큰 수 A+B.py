# n, m = map(str, input().split())
#
# n = ''.join(reversed(n))
# m = ''.join(reversed(m))
# result = []
#
# if len(n) < len(m):
#     str_len = len(n)
#     max_len = len(m)
#     max_str = m
# else:
#     str_len = len(m)
#     max_len = len(n)
#     max_str = n
#
# up = 0
# for i in range(str_len):
#     if int(n[i]) + int(m[i]) + up < 10:
#         result.append(str(int(n[i]) + int(m[i]) + up))
#         up = 0
#     else:
#         result.append(str(int(n[i]) + int(m[i]) + up - 10))
#         up = 1
#
# for i in range(str_len, max_len):
#     if up == 1:
#         result.append(str(int(max_str[i]) + 1))
#         up = 0
#     else:
#         result.append(max_str[i])
# if up == 1:
#     result.append(str(1))
#
# result = ''.join(reversed(result))
# for i in range(len(result)):
#     print(int(result[i]), end="")

n, m = map(int, input().split())
print(n + m)