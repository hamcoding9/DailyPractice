import copy 
n = int(input())
graph = []
for i in range(n):
    graph.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
    
def dfs(graph:list, line:list, x:int, y:int):
    stack = list()
    stack.append((x, y))
    graph[x][y] = '0'
    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] in line:
                stack.append((nx, ny))
                graph[nx][ny] = '0'
                
# 적록색약 아닌 사람
section, blue = 0, 0 # blue는 이후 재활용할 수 있으므로 따로 저장
copied_graph = copy.deepcopy(graph)
for i in range(n):
    for j in range(n):
        if copied_graph[i][j] == 'R':
            dfs(copied_graph, ['R'], i, j)
            section += 1
        if copied_graph[i][j] == 'G':
            dfs(copied_graph, ['G'], i, j)
            section += 1
        if copied_graph[i][j] == 'B':
            dfs(copied_graph, ['B'], i, j)
            section += 1
            blue += 1
print(section, end=' ')

# 적록색약인 사람
section = 0
section += blue
for i in range(n):
    for j in range(n):
        if graph[i][j] in ['R', 'G']:
            dfs(graph, ['R', 'G'], i, j)
            section += 1
print(section)

'''
내가 푼 방법:
1. 먼저 적록색약이 아닌 사람의 구획을 찾는다.
'R', 'G', 'B'일 때 각각의 개수를 더한다.
2. 다음으로, 적록색약인 사람의 구획을 찾는다.
['R', 'G'], 'B'일 때 각각의 개수를 더한다.
3. 이때 'B'의 개수는 따로 저장해 두었다가 재활용한다.

다른 방법 
1. 'R'을 전부 'G'로 바꾼다. (그 반대도 Ok)
2. dfs 진행 과정에서 조건을 x,y 색 == nx,ny 색으로 한다.
3. graph를 copy해서 두 번 만들지 않고 visit 리스트를 활용한다.
'''
