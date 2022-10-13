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