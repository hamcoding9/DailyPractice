def solution(A, B):
    answer, ptr1, ptr2 = 0, 0, 0
    A.sort()
    B.sort()
    while ptr2 < len(B):
        if A[ptr1] < B[ptr2]:
            ptr1 += 1
            answer += 1
        ptr2 += 1
    return answer