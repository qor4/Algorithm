def solution(n, computers):
    graph = []
    answer = 0
    for i in range(n):
        graph.append([j for j in range(n) if computers[i][j] == 1 and i != j])
    print(graph)
    confirm = []
    for i in range(n):
        if i not in confirm:
            visit = []
            stack = [i]
            while stack:
                computer = stack.pop()
                if computer not in visit:
                    confirm.append(computer)
                    visit.append(computer)
                    stack.extend(graph[computer])
            answer += 1
    return answer
