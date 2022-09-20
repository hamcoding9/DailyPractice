# 1. 재귀 버전
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(start, end):
            if start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return binary_search(start,  mid - 1)
                else:
                    return binary_search(mid + 1, end)
            else:
                return -1
        return binary_search(0, len(nums) - 1)
    
# 2. Loop 버전
def search(self, nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

# 3. 파이썬에 있는 이진 검색 모듈
def search(self, nums: List[int], target: int) -> int:
    index = bisect.bisect_left(nums, target)
    
    if index < len(nums) and nums[index] == taret:
        return index
    else:
        return -1
