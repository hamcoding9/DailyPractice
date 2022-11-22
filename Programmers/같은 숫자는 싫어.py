# 첫 번째 방법. 정확도100 / 시간초과
def solution(arr):
    for i in range(len(arr) - 1):
        if arr[i] == arr[i+1]:
            arr[i] = 10
    while 10 in arr:
        arr.remove(10)
    return arr

# 두 번째 방법 시간초과
def solution(arr):
    index = 0
    while True:
        if index == len(arr)-1:
            break
        else:
            if arr[index] == arr[index+1]:
                del arr[index]
                index = index-1
            index += 1
    return arr

