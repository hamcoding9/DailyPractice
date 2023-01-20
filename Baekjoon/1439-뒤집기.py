# 몇몇 케이스에서 시간 초과가 나온다.
# 더 적은 양의 숫자가 시작과 끝에 있을 경우 전체 숫자를 계속 뒤집으면서 무한 반복이 되기 때문인 것 같다.
# 해결책을 더 고민해보자...

num = list(map(int, list(input())))

count = 0

def is_same(numbers: list) -> bool:
    n = numbers[0]
    for num in numbers:
        if n != num:
            return False
    return True

def reverse_number(numbers, start_index, end_index):
    for i in range(start_index, end_index):
        if numbers[i] == 0:
            numbers[i] = 1
        else:
            numbers[i] = 0

while not is_same(num):
    if num.count(1) >= num.count(0):
        start_index = num.index(0)
        end_index = len(num) - list(reversed(num)).index(0)
        reverse_number(num, start_index, end_index)
    else:
        start_index = num.index(1)
        end_index = len(num) - list(reversed(num)).index(1)
        reverse_number(num, start_index, end_index)
    count += 1

print(count)