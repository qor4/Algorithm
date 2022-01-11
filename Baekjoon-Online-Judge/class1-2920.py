import sys

data = list(map(int, sys.stdin.readline().strip().split()))
def ascending(data):
    num = data[0]
    for i in range(1, 8):
        if num + 1 != data[i]:
            print("mixed")
            exit()
        num = data[i]
    print("ascending")


def descending(data):
    num = data[0]
    for i in range(1, 8):
        if num - 1 != data[i]:
            print("mixed")
            exit()
        num = data[i]

    print("descending")

if data[0] == 1:
    ascending(data)

elif data[0] == 8:
    descending(data)
else:
    print("mixed")