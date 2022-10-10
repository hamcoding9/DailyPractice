# Status: on-going
# 답은 맞게 나오나 시간이 너무 오래 걸림
from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 바이러스 퍼뜨리기
def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 2
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 2
    return

# 벽을 세우는 경우의 수
def make_case(graph):
    basket = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                basket.append((i, j))
    return list(combinations(basket, 3))

safe_area = []

walls = make_case(graph)
while walls:
    graph_copy = copy.deepcopy(graph)
    wall_case = walls.pop()
    for w in wall_case:
        graph_copy[w[0]][w[1]] = 1
    for i in range(n):
        for j in range(m):
            if graph_copy[i][j] == 2:
                bfs(graph_copy, i, j)
    safe = sum(map(lambda x: x.count(0), graph_copy))
    safe_area.append(safe)
    
print(max(safe_area))