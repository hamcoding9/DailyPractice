def solution(genres, plays):
    answer = []
    dict1, dict2 = {}, {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        dict1[g] = dict1.get(g, 0) + p
        dict2[g] = dict2.get(g, []) + [(i, p)]
    
    for (k, v) in sorted(dict1.items(), key = lambda x:x[1], reverse = True):
        for (i, p) in sorted(dict2[k], key = lambda x:x[1], reverse= True)[:2]:
            answer.append(i)

    return answer