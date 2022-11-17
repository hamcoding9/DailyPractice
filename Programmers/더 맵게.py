# 내 풀이
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) 
    while True:
        if scoville[0] >= K: 
            return answer
        elif len(scoville) > 1:
            new_food = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
            heapq.heappush(scoville, new_food)
            answer += 1
        else:
            return -1

# 다른 풀이
# 분기가 훨씬 직관적이다!
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + min2 * 2
        heapq.heappush(scoville, new_scoville)
        answer += 1
    return answer