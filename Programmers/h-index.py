# 처음 풀이 버전
# 테스트 케이스 11, 16 통과 못함
def solution(citations):
    citations.sort(reverse=True)
    max_num = min(citations[0], len(citations))
    for h in range(max_num, -1, -1):
        for i, c in enumerate(citations):
            if c < h:
                if i == h:
                    return h
                else:
                    break
    return len(citations) - h

# 개선한 풀이
def solution(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if c <= i:
            return i
    return len(citations)