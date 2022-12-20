def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i != 0:
            continue
        l, w = i, yellow / i
        if w < l: 
            break
        b = 2 * (l + w) + 4
        if b == brown:
            break
    return [w + 2, l + 2]