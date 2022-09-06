from collections import Counter
def solution(participant, completion):
    uncompleted = Counter(participant) - Counter(completion)
    return list(uncompleted)[0]
