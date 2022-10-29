# 시간 초과가 나오는 상황
N = int(input())

# current_row: 한 행에 한 개씩 배치하므로 현재 행에 대한 정보
# current_candidate: 현재까지 배치된 퀸의 위치 정보
def DFS(N : int, current_row : int, current_candidate: list, final_result: list) :
    if current_row == N:
        final_result.append(current_candidate[:])
        return
    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate, final_result)
            current_candidate.pop()

def is_available(candidate: list, current_col: int) -> bool:
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col)==abs(current_row - queen_row): # 수직 검사 + 대각선 검사
            return False
    return True

def solve_n_queen(N : int) -> int:
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result

print(len(solve_n_queen(N)))

# 두 번째 풀이
# 또 시간 초과임 (대체...ㅡㅡ)

N = int(input())
row = [0] * N
result = 0

def is_available(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def DFS(x): # x = 행
    global result
    if x == N: 
        result += 1 # 경우의 수 추가
        return
    else:
        for i in range(N): 
            row[x] = i # 각 행에 말 놓기
            if is_available(x):
                DFS(x + 1)

DFS(0)
print(result)