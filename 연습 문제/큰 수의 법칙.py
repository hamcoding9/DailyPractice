# number list와 m, k가 모두 주어졌다고 가정
def solution(l: list, m: int, k: int) -> int:
    l.sort(reverse=True)
    answer = 0
    pre = (l[0] * k) * (m // (k + 1))
    pre += l[1] * (m // (k + 1))
    post = l[0] * (m % (k + 1))
    answer = pre + post
    return answer

# 테스트
l = [2, 4, 5, 4, 6]
m = 8
k = 3
print(solution(l, m, k)) # 46

l = [3, 4, 3, 4, 3]
m = 7
k = 2
print(solution(l, m, k)) # 28