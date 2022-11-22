def solution(a, b):
    temp = list(map(lambda x, y: x * y, a, b))
    answer = sum(temp)
    return answer

def solution(a, b):
    return sum([x * y for x, y in zip(a, b)])