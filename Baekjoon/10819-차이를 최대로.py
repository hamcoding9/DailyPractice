from itertools import permutations

n = int(input())
numbers = list(map(int, input().split(' ')))

cases = list(permutations(numbers, n))
diff_list = []
for case in cases:
    diff = 0
    for index in range(1, n):
        diff += abs(case[index - 1] - case[index])
    diff_list.append(diff)

print(max(diff_list))