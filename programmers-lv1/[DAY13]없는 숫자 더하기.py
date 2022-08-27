def solution(numbers):
    return sum({0, 1, 2, 3, 4, 5, 6, 7, 8, 9} - set(numbers))

# 더 간결하게
def solution(numbers):
    return sum(range(10)) - sum(numbers)