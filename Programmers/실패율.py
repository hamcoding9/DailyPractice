# 처음 짠 코드 -> 몇 가지 테스트 케이스에서 런타임 오류 발생
from bisect import bisect_right
def solution(N, stages):
    answer = dict()
    stages.sort()
    players_len = len(stages)
    for stage in range(1, N + 1):
        arrived = players_len - bisect_right(stages, stage - 1)
        success = players_len - bisect_right(stages, stage)
        fail = arrived - success
        rate = fail / arrived
        answer[stage] = rate
    sorted_item = sorted(answer.items(), key=lambda x:-x[1])
    answer = []
    for item in sorted_item:
        answer.append(item[0])
    return answer

# 다른 사람의 코드를 참고해서 다시 풀이
def solution(N, stages):
    answer = []
    player = len(stages)
    for stage in range(1, N+1):
        count = stages.count(stage)
        if player == 0:
            fail = 0
        else:
            fail = count / player
        player -= count
        answer.append((stage, fail))
    answer.sort(key=lambda x:-x[1])
    answer = [i[0] for i in answer]
    return answer