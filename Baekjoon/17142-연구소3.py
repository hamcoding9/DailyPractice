from itertools import combinations
from collections import deque

n, m = map(int, input().split())
graph = []
virus_index = []
target = 0

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 2:
            virus_index.append((i, j))
        if graph[i][j] == 0:
            target += 1 # 전부 감염시켜야 함

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(combination: list) -> int:
    global answer
    queue = deque()
    visited = [([-1] * n) for _ in range(n)]
    infected = 0 # 감염시킨 횟수
    for i in combination:
        queue.append(i)
        visited[i[0]][i[1]] += 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if cx < 0 or cx >= n or cy < 0 or cy >= n:
                continue
            if graph[cx][cy] != 1 and visited[cx][cy] == -1:
                visited[cx][cy] = visited[x][y] + 1
                queue.append((cx, cy))
                if graph[cx][cy] == 0:
                    infected += 1
    max_duration = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                max_duration = max(max_duration, visited[i][j])
    if infected == target:
        answer = min(answer, max_duration)


# 바이러스를 활성시키는 경우의 수 담기
c_virus = list(combinations(virus_index, m))

# 모든 경우의 수 다 세어보기
result = []
answer = int(1e9)
for combination in c_virus:
    a = bfs(combination)

if answer == int(1e9):
    print(-1)
else:
    print(answer)