# 1) 정확도100 / 시간초과
def solution(n):
    answer = 0
    for element in range(1, n+1):
        if len([i for i in range(1, (element//2)+1) if element%i==0]) ==1:
            answer+=1
    return answer