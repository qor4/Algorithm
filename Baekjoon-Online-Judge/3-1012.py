import sys
input = sys. stdin.readline

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    cnt = 0
    li = []
    queue = []
    for _ in range(k):
        x, y = map(int, input().split())
        li.append([x, y])

    while li:
        node = li.pop(0)
        queue.append(node)
        temp = [node[0], node[1] - 1], [node[0] - 1, node[1]], [node[0] + 1, node[1]], [node[0], node[1] + 1]
        state = 1
        for i in temp:
            if i in li:
                queue.append(i)
                li.pop(li.index(i))
                state = 0
            elif i in queue:
                state = 0
        if state:
            queue = []
            state = 1
            cnt += 1