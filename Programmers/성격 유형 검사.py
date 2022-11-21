def solution(survey, choices):
    type_dict = {1:{'R':0, 'T':0}, 2:{'C':0, 'F':0},
                3:{'J':0, 'M':0}, 4:{'A':0, 'N':0}}
    for s, c in zip(survey, choices):
        if s in ["RT", "TR"]:
            if c > 4:
                type_dict[1][s[1]] += abs(c - 4)
            elif c < 4:
                type_dict[1][s[0]] += abs(c - 4)
        if s in ["CF", "FC"]:
            if c > 4:
                type_dict[2][s[1]] += abs(c - 4)
            elif c < 4:
                type_dict[2][s[0]] += abs(c - 4)
        if s in ["JM", "MJ"]:
            if c > 4:
                type_dict[3][s[1]] += abs(c - 4)
            elif c < 4:
                type_dict[3][s[0]] += abs(c - 4)
        if s in ["AN", "NA"]:
            if c > 4:
                type_dict[4][s[1]] += abs(c - 4)
            elif c < 4:
                type_dict[4][s[0]] += abs(c - 4)
    answer = ""
    for (key, value) in type_dict.items():
        for (k, v) in sorted(value.items(), key = lambda x: (-x[1], x[0])):
            answer += k
    return answer[0:8:2]