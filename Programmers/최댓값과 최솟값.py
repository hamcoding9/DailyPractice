def solution(s):
    split_list = list(map(int, s.split(" ")))
    answer = str(min(split_list)) + " " + str(max(split_list))
    return answer