def solution(d, budget):
    # 초기화
    answer = 0
    # 오름차순 정렬
    d.sort()
    # answer 찾기
    for i in range(len(d)):
        if(budget >= d[i]):
            budget -= d[i]
            answer += 1
        else:
            return answer
    return answer 
    
# test case
d = [2, 2, 3, 3]
budget = 10
result = solution(d, budget)
print(result)