n, x = map(int, input().split())

list = list(map(int, input().split()))
len = len(list)
for i in range(0, len):
    if(list[i] < x):
        print(list[i], " ", end = "", sep = "")