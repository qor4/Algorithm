num_t = int(input())
for i in range(num_t):
    num_r, str_s = map(str, input().split())
    for j in range(len(str_s)):
        for k in range(int(num_r)):
            print(str_s[j], end = "")
    print()

