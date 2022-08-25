# 첫 번째 방법 => 시간 초과
def solution(participant, completion):
    for ppl in completion:
        participant.remove(ppl)
    return participant[0]

# 두 번째 방법

