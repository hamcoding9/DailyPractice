from bisect import bisect_left, bisect_right

def binary_search(array:list, target:int) -> int:
    start, end = 0, len(array) - 1
    count = 0
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] == target:
            del array[mid]
            count += 1
            end -= 1
    return count

n, target = map(int, input().split())
array = list(map(int, input().split()))

count = binary_search(array, target)

if count > 0:
    print(count)
else:
    print(-1)

# 라이브러리를 활용한 풀이
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index