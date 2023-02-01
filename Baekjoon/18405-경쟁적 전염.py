from collections import deque

n, k = map(int, input().split())
graph, virus = [], []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j, 0))

target_s, target_x, target_y = map(int, input().split())

virus.sort(key=lambda x:x[0])
queue = deque(virus)

while queue:
    v, x, y, s = queue.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = v
            queue.append((v, nx, ny, s+1))

print(graph[target_x-1][target_y-1])