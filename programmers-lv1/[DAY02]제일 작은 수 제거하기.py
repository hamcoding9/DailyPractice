def solution(arr):
    arr.remove(min(arr))
    if len(arr) > 0:
        return arr
    else:
        return [-1]