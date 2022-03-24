import sys

jdq = []
fdq = []
dxy = [(-1, 0), (0, 1), (0, -1), (1, 0)]
r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for i in range(r)]

jvisit = [[0 for i in range(c)] for i in range(r)]
fvisit = [[0 for i in range(c)] for i in range(r)]

jbool = True
for i in range(r):
    for j in range(c):
        if board[i][j] == 'J':
            jdq.append((i, j))
            jvisit[i][j] = 1
        elif board[i][j] == 'F':
            fdq.append((i, j))
            fvisit[i][j] = 1


def jsearch(jdq):
    global jbool
    dq = []
    for idx in jdq:
        for x, y in dxy:
            nx = idx[0] + x
            ny = idx[1] + y
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                jbool = False
                continue
            if board[nx][ny] == ".":
                board[nx][ny] = 'J'
                if jvisit[nx][ny] != 1:
                    dq.append((nx, ny))
                    jvisit[nx][ny] = 1
    return dq

def fsearch(fdq):
    dq = []
    for idx in fdq:
        for x, y in dxy:
            nx = idx[0] + x
            ny = idx[1] + y
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if board[nx][ny] != "#":
                board[nx][ny] = 'F'
                if fvisit[nx][ny] != 1:
                    dq.append((nx, ny))
                    fvisit[nx][ny] = 1
    return dq


cnt = 0
while jbool and jdq:
    fdq = fsearch(fdq)
    jdq = jsearch(jdq)
    cnt += 1


print(cnt) if not jbool else print("IMPOSSIBLE")

