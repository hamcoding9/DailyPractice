def solution(tickets):
    graph = {}
    for i in tickets:
        graph[i[0]] = graph.get(i[0], []) + [i[1]]
    for i in graph:
        graph[i].sort(reverse=True) # 알파벳 내림차순으로 정렬
    stack = ["ICN"]
    route = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in graph or len(graph[top])==0:
            route.append(stack.pop())
        else:
            stack.append(graph[top][-1])
            graph[top] = graph[top][:-1]
    return route[::-1] # 다시 알파벳 오름차순으로 정렬