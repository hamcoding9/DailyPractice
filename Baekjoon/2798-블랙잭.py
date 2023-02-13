from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))

types = list(combinations(range(n), 3))

max_value = 0
for type in types:
    answer = nums[type[0]] + nums[type[1]] + nums[type[2]]
    if answer <= m:
        max_value = max(max_value, answer)

print(max_value)