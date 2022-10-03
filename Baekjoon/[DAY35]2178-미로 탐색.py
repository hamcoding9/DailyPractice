from collections import deque

n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input())))
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if maze[nx][ny] == 1: # 처음 방문하면 거리 + 1 추가
                maze[nx][ny] = maze[cx][cy] + 1
                queue.append((nx, ny))
                
    return maze[n-1][m-1] # 도착 지점에서의 최단거리 반환
    
print(bfs(0, 0))
