import sys
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]
cost = [[0 for _ in range(v+1)] for _ in range(v+1)]
def dfs(v):
    queue = []
    queue.append(i)
    visit = []
    while queue:
        node = queue.pop(0)

for _ in range(v):
    node = list(map(int, input().split()))[:-1]
    for i in range(1, len(node)-1, 2):
        graph[node[0]].append([node[i], node[i+1]])


for i in range(1, v+1):
    dfs(i)

print(graph)