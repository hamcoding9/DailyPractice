# 단지 번호 붙이기 이번엔 dfs로 풀어보자!
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
def dfs(x, y):
    stack = list()
    stack.append((x, y))
    graph[x][y] = 0
    count = 1
    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            if graph[nx][ny] == 1:
                stack.append((nx, ny))
                graph[nx][ny] = 0 # 방문 처리
                count += 1
    return count

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(dfs(i, j))

cnt.sort()
print(len(cnt))
for c in cnt:
    print(c)
