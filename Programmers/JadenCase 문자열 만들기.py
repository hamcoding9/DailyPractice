def solution(s):
    answer = [i.capitalize() for i in s.split(" ")]
    return " ".join(answer)