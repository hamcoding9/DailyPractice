# 행렬을 90도 회전시켜주는 함수
def rotate_matrix_by_90_degree(matrix):
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            new_matrix[j][n-i-1] = matrix[i][j]
    return new_matrix

# 열쇠가 자물쇠에 들어가는지 확인하는 함수
# padded_lock에서 실제 lock이 존재하는 부분이 모두 1이면 열쇠가 맞는다는 것을 의미
def is_unlock(padded_lock):
    n = len(padded_lock) // 3
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if padded_lock[i][j] != 1:
                return False
    return True

# solution
def solution(key, lock):
    n = len(lock)
    m = len(key)
    padded_lock = [[0] * (n * 3) for i in range((n * 3))]
    # 패딩 처리한 자물쇠 배열의 중간에 실제 자물쇠를 넣는다
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            padded_lock[i][j] = lock[i-n][j-n]
    # 총 4번 회전하며 완전 탐색 수행
    for rotation in range(4):
        key = rotate_matrix_by_90_degree(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        padded_lock[x+i][y+j] += key[i][j]
                if is_unlock(padded_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        padded_lock[x+i][y+j] -= key[i][j]
    return False    