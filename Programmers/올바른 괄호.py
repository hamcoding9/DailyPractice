# 모든 경우의 수를 고려한 버전
def solution(s):
    if s[0] == ")":
        return False
    uncompleted = 0
    for b in s:
        if uncompleted < 0:
            return False
        if b == "(":
            uncompleted += 1
        else:
            uncompleted -= 1
    return (uncompleted == 0)

# 스택/큐를 사용한 버전
from collections import deque
def solution(s):
    d = deque()
    for b in s:
        if b == "(":
            d.append(b)
        else:
            if len(d) <= 0:
                return False
            d.pop()
    return (len(d) == 0)