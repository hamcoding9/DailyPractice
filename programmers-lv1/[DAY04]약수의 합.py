def solution(n):
    div = []
    for i in range(1, (n+1)):
        if n%i==0:
            div.append(i)
    return sum(div)

# 줄이기
def solution(n):
    return sum([i for i in range(1, n+1) if n%i==0])

# 1/2
def solution(n):
    return n + sum([i for i in range(1, (n//2)+1) if n%i==0])