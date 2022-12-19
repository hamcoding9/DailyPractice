def solution(s):
    count = 0
    zero_count = 0
    while s != "1":
        zero = 0
        s_list = list(s)
        for num in s_list:
            if num == "0":
                zero += 1
        new_num = len(s) - zero
        s = bin(int(new_num))[2:]
        count += 1
        zero_count += zero
    answer = [count, zero_count]
    return answer