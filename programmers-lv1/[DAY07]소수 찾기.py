# 시도 2: 또 시간초과
def isprime(x):
    for i in range(2, int(x**1/2)+1):
        if x % i == 0:
            return False
    return True

def solution(n):
    return len([i for i in range(2, n+1) if isprime(i)])
  
# 시도3: 에라토스테네스의 체를 활용
# 이게 유도된 정답이었나 싶다. ㅠㅠ.
def solution(n):
    N = set(range(2, n+1))
    for i in range(2, n+1):
        if i in N:
            N-=set(range(2*i, n+1, i))
    return len(N)
