def solution(n, lost, reserve):
    uniform = [1] * (n+2)
    for student in reserve:
        uniform[student] += 1
    for student in lost:
        uniform[student] -= 1
    for i in range(1, n+1):
        if uniform[i-1] == 0 and uniform[i] == 2:
            uniform[i-1], uniform[i] = 1, 1
        elif uniform[i+1] == 0 and uniform[i] == 2:
            uniform[i+1] , uniform[i] = 1, 1
    attend = [i for i, v in enumerate(uniform) if v>0]
    answer = len(attend) - 2
    return answer

# set을 활용한 풀이
def solution(n, lost, reserve):
    have_uniform = set(lost) & set(reserve)
    lost_uniform = set(lost) - have_uniform
    reserve_uniform = set(reserve) - have_uniform
    for i in sorted(reserve_uniform):
        if i - 1 in lost_uniform:
            lost_uniform.remove(i - 1)
        elif i + 1 in lost_uniform:
            lost_uniform.remove(i + 1)
    return n - len(lost_uniform)