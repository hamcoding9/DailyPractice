def solution(x):
    return not x % sum([int(i) for i in str(x)])
