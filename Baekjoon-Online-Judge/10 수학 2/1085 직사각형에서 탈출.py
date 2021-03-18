x, y, w, h = map(int, input().split())

num = [x, w-x, y, h-y]
num.sort()
print(num[0])
