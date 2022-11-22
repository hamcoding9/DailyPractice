# 첫 번째 방법
def solution(a, b):
    return sum([i for i in range(a,b+1)]) if a<b else sum([i for i in range(b, a+1)])

# 두 번째 방법
def solution(a, b):
    if a > b : a, b = b, a
    return sum(range(a, b+1))
  
# 세 번째 방법
def solution(a, b):
    return sum(range(min(a, b), max(a, b)+1))
