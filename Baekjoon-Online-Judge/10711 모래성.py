import sys
from collections import deque

dxy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

h, w = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(h)]
dq = deque()

for i in range(h):
    for j in range(w):
        if board[i][j] == '.':
            board[i][j] = 0
            dq.append((i, j, 0))
        else:
            board[i][j] = int(board[i][j])

while dq:
    index = dq.popleft()
    cnt = index[2]
    for x, y in dxy:
        nx = index[0]+x
        ny = index[1]+y
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if board[nx][ny] != 0:
            board[nx][ny] -= 1
            if board[nx][ny] == 0:
                dq.append((nx, ny, cnt+1))


print(cnt)
