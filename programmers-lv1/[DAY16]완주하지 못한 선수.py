# 두 개 이상의 리스트 => zip() 활용
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p    
    return participant[-1]
