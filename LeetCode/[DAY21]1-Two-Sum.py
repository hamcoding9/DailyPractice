# 1. Two Sum
# Memory Limit Exceeded
# Brute-Force
from itertools import combinations
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in list(combinations(range(len(nums)), 2)):
            if nums[index[0]] + nums[index[1]] == target:
                return list(index)
              
# Another Version
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            if (target-n) in nums[i+1:]:
                return [i, nums[i+1:].index(target-n) + (i + 1)]
