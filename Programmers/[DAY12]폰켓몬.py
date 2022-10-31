def solution(nums):
    nums_set = set(nums)
    return len(nums_set) if len(nums_set) <= (len(nums)/2) else len(nums)/2
  
# 더 간결한 방법
def solution(nums):
  return min(len(nums)/2, len(set(nums)))
