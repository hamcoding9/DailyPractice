# 첫 번째 방법
def solution(array, commands):
    answer = []
    for n in range(len(commands)):
        i, j, k = commands[n]
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

# map() + lambda 활용한 두 번째 방법
def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))