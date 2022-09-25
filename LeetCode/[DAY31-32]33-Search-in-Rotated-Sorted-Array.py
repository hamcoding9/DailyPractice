# my solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums:List[int], target:int) -> int:
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        nums_sort = sorted(nums)
        t_idx = binary_search(nums_sort, target)
        if t_idx == -1:
            return -1
        else:
            pivot_idx = binary_search(nums_sort, nums[0])
            return t_idx-pivot_idx if t_idx >= pivot_idx else t_idx+(len(nums)-pivot_idx)

# DAY 32
# Another Version of #33
# return has been modified
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums:List[int], target:int) -> int:
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        nums_sort = sorted(nums)
        t_idx = binary_search(nums_sort, target)
        if t_idx == -1:
            return -1
        else:
            pivot_idx = binary_search(nums_sort, nums[0])
            jump = len(nums)-pivot_idx
            return (t_idx+jump)%len(nums)
