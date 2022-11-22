# 첫 번째 방법
def solution(n):
    sqrt = n**(1/2)
    if int(n**(1/2)) == n**(1/2):
        return (int(n**(1/2)) + 1)**2
    else:
        return -1

# 두 번째 방법
def solution(n):
    sqrt = n**(1/2)
    return (sqrt+1)**2 if int(sqrt)==sqrt else -1