def solution(s: str) -> int:
    n = len(s)
    min_length = len(s)
    for step in range(1, n//2+1):
        compressed = ""
        chunk = s[:step]
        count = 1
        for i in range(step, n, step):
            if chunk == s[i:i+step]:
                count += 1
            else:
                compressed += str(count) + chunk if count >= 2 else chunk
                chunk = s[i:i+step]
                count = 1
        compressed += str(count) + chunk if count >=2 else chunk
        min_length = min(min_length, len)
    return min_length

a = "aabbaccc"
b = "ababcdcdababcdcd"
c = "abcabcdede"
d = "abcabcabcabcdededededede"
e = "xababcdcdababcdcd"

print(solution(a))
print(solution(b))
print(solution(c))
print(solution(d))
print(solution(e))