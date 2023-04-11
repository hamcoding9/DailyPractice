def solution(k, tangerine):
    size = dict()
    for t in tangerine:
        size[t] = size.get(t, 0) + 1
    size = sorted(size.items(), key=lambda x:-x[1])
    count = 0
    for i in range(len(size)):
        if count >= k:
            return i
        count += size[i][1]
    return len(size)