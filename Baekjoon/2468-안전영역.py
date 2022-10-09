# status: on-going
# 아직 다 풀지 못함! 
import copy 

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(graph, x, y):
    stack = list()
    stack.append((x, y))
    graph[x][y] = 0 # 그래프에 방문 처리
    count = 1
    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            if graph[nx][ny] > sink:
                stack.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    return count

# sink = 4
# cnt = []
# for j in range(n):
#     for k in range(n):
#         if graph[j][k] > sink:
#             cnt.append(dfs(j,k))
# print(len(cnt))
                
safe_area = []
for i in range(1, max(map(max, graph))+1): # 모든 sink 경우를 고려
    sink = i
    cnt = [] # 안전한 영역을 담음
    g = copy.deepcopy(graph) # graph를 복사함
    for j in range(n):
        for k in range(n):
            if graph[j][k] > sink:
                cnt.append(dfs(g, j,k))
    safe_area.append(len(cnt))
    
print(safe_area)
