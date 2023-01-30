from collections import deque

n, m, k, x = map(int,input().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

queue = deque()
queue.append(x)

while queue:
    cur = queue.popleft()
    for element in graph[cur]:
        if distance[element] == -1:
            queue.append(element)
            distance[element] = distance[cur] + 1

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)