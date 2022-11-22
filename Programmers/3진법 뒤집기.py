def solution(n):
    ternary = ""
    while n > 0:
        ternary += str(n%3)
        n//=3
    return sum([int(t)*pow(3,int(idx)) for idx, t in enumerate(ternary[::-1])])

# int 함수를 사용한 경우(다른 사람 풀이)
def solution(n):
    ternary = ""
    while n:
        ternary += str(n%3)
        n//=3
    return int(ternary, 3)