# 아직 다 못 풀었음
# 예제 1, 2만 통과
# move에 문제 있는 것 같음..
n, m = map(int, input().split())
graph, blizzard = [], []
for i in range(n):
    graph.append(list(map(int, input().split())))
for i in range(m):
    _d, _s = map(int, input().split())
    blizzard.append((_d - 1, _s))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
bomb = [] # 폭발한 구슬 저장

nums = dict()
# 번호에 따른 index 위치 저장
def save_nums():
    global nums, n
    count = 1
    cx, cy = n//2, n//2
    step, direction, rotate, target_step = 0, 0, 0, 1
    _dx = [0, 1, 0, -1]
    _dy = [-1, 0, 1, 0]
    while count < n * n:
        if step == target_step:
            direction = (direction + 1) % 4
            step = 0
            rotate += 1
        if rotate == 2:
            rotate = 0
            target_step += 1
        nx = cx + _dx[direction]
        ny = cy + _dy[direction]
        nums[count] = (nx, ny)
        step += 1
        cx, cy = nx, ny
        count += 1

def move_backward(count: int):
    global graph, nums, n, bomb
    while count < n * n - 1:
        cx, cy = nums[count]
        nx, ny = nums[count + 1]
        graph[cx][cy] = graph[nx][ny]
        count += 1

def move(c):
    global graph, nums, n, bomb
    count = 1
    for _ in range(c):
        for count in range(1, n * n):
            cx, cy = nums[count]
            if graph[cx][cy] == 0: # 구슬이 비었다면
                move_backward(count) # 앞으로 한칸씩 이동

def chain_bomb():
    global graph, nums, n, bomb
    chain = 0 # 이전 턴의 구슬 번호 저장
    chain_list = [] # 연속하는 경우 위치 저장
    while True:
        is_bomb = False
        chain_bomb_count = 0
        for count in range(1, n * n):
            cx, cy = nums[count]
            if chain != graph[cx][cy]:
                if len(chain_list) >= 4 and chain > 0:
                    is_bomb = True
                    for c in chain_list:
                        bomb.append(chain)
                        graph[c[0]][c[1]] = 0
                        chain_bomb_count += 1
                chain_list = []
            chain_list.append((cx, cy))
            chain = graph[cx][cy]
        if is_bomb:
            move(chain_bomb_count)
        else:
            return
        
def change():
    global graph, nums, n, bomb
    new_graph = [[0]*n for i in range(n)]
    chain = graph[nums[1][0]][nums[1][1]] # 이전 턴의 구슬 번호 저장
    chain_count = 0 # 그룹 안에 구슬 개수 저장
    new_count = 1 # 새 그래프에 저장하기 위한 count
    count = 1 # 현재 그래프를 순회하는 count
    while new_count < n*n-1 and count < n*n:
        cx, cy = nums[count]
        if chain != graph[cx][cy]:
            a = chain_count
            b = chain
            new_graph[nums[new_count][0]][nums[new_count][1]] = a
            new_graph[nums[new_count+1][0]][nums[new_count+1][1]] = b
            new_count += 2
            chain_count = 1
            chain = graph[cx][cy]
            count += 1
            continue
        chain = graph[cx][cy]
        chain_count += 1
        count += 1
    graph = new_graph

save_nums()
while blizzard:
    d, s = blizzard.pop(0)
    cx, cy = n//2, n//2
    bomb_count = 0
    for i in range(s):
        nx = cx + dx[d]
        ny = cy + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        bomb_count += 1
        graph[nx][ny] = 0 # 구슬 떨어짐
        cx, cy = nx, ny
    print(graph)
    move(bomb_count) # 구슬 이동
    print(graph)
    chain_bomb() # 연속하는 구슬 폭발 -> 이동 반복
    print(graph)
    change() # 구슬 변화
    print(graph)

print(bomb)
count_1 = bomb.count(1)
count_2 = bomb.count(2)
count_3 = bomb.count(3)
result = count_1 + 2*count_2 + 3*count_3
print(result)