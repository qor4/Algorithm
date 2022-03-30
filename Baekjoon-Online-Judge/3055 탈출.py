import sys

wdq = []
sdq = []
dxy = [(-1, 0), (0, 1), (0, -1), (1, 0)]
r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for i in range(r)]

svisit = [[0 for i in range(c)] for i in range(r)]
wvisit = [[0 for i in range(c)] for i in range(r)]

jbool = True
for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            sdq.append((i, j))
            svisit[i][j] = 1
        elif board[i][j] == '*':
            wdq.append((i, j))
            wvisit[i][j] = 1


def ssearch(jdq):
    global jbool
    dq = []
    for idx in jdq:
        for x, y in dxy:
            nx = idx[0] + x
            ny = idx[1] + y
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if board[nx][ny] == 'D':
                jbool = False
                continue
            elif board[nx][ny] == ".":
                board[nx][ny] = 'S'
                if svisit[nx][ny] != 1:
                    dq.append((nx, ny))
                    svisit[nx][ny] = 1
    return dq

def wsearch(fdq):
    dq = []
    for idx in fdq:
        for x, y in dxy:
            nx = idx[0] + x
            ny = idx[1] + y
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if board[nx][ny] == 'S' or board[nx][ny] == '.':
                board[nx][ny] = '*'
                if wvisit[nx][ny] != 1:
                    dq.append((nx, ny))
                    wvisit[nx][ny] = 1
    return dq


cnt = 0
while jbool and sdq:
    wdq = wsearch(wdq)
    sdq = ssearch(sdq)
    cnt += 1


print(cnt) if not jbool else print("KAKTUS")

