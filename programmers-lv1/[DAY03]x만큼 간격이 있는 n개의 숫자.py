# 첫 번째 방법
def solution(x, n):
    answer = []
    difference = x
    for i in range(n):
        answer.append(x)
        x += difference
    return answer

# 두 번째 방법
def solution(x, n):
    return [num+(x*idx) for idx, num in enumerate([x]*n)]