from collections import deque 

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(maps, x, y):
    queue = deque()
    n, m = len(maps), len(maps[0])
    queue.append((x, y))
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[cx][cy] + 1
                queue.append((nx, ny))
    return maps[n - 1][m - 1]

def solution(maps):
    answer = dfs(maps, 0, 0)
    return answer if answer > 1 else -1