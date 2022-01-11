import sys
input = sys.stdin.readline

n = int(input().strip())
k = int(input().strip())

graph = [[] for _ in range(n+1)]
for _ in range(k):
    node1, node2 = map(int, input().strip().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

stack = []
visit = []
stack.append(1)

while stack:
    node = stack.pop()
    if node not in visit:
        visit.append(node)
        stack.extend(graph[node])

print(len(visit)-1)