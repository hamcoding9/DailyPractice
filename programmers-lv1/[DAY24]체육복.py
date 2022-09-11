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
