# 첫 번째 방법
def solution(num):
    cnt = 0
    for i in range(500):
        if num == 1:
            return cnt
        elif num % 2 == 0:
            num //= 2
            cnt += 1
        else:
            num  = num * 3 + 1
            cnt += 1
    return -1

# 두 번째 방법
def solution(num):
    cnt = 0
    for i in range(500):
        if num == 1:
            return cnt
        num = num//2 if num%2==0 else num*3+1
        cnt+=1
    return -1
