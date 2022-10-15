import copy 

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, visit):
    stack = list()
    stack.append((x, y))
    visit[x][y] = 1 # 그래프에 방문 처리
    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            if graph[nx][ny] > sink and visit[nx][ny] == 0:
                stack.append((nx, ny))
                visit[nx][ny] = 1
                
safe_area = []
for i in range(max(map(max, graph))+1): # 모든 sink 경우를 고려(아무 지역도 물에 잠기지 않는 경우를 고려해서 0도 포함)
    count = 0
    sink = i
    visit = [[0]*n for i in range(n)]
    for j in range(n):
        for k in range(n):
            if graph[j][k] > sink and visit[j][k]==0:
                dfs(j, k, visit)
                count += 1
    safe_area.append(count)

print(max(safe_area))