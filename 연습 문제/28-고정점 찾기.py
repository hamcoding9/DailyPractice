def binary_search(array):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if mid > array[mid]:
            start = mid + 1
        elif mid < array[mid]:
            end = mid - 1
        else:
            return mid
    return -1

n = int(input())
array = list(map(int, input().split()))
print(binary_search(array))