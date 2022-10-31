def solution(absolutes, signs):
    return sum([i if j else i*(-1) for i, j in zip(absolutes, signs)])