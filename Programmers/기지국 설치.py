# 효율성 테스트까지 통과
def solution(n, stations, w):
    uncovered = []
    for i in range(1, len(stations)):
        area = (stations[i] - w - 1) - (stations[i - 1] + w)
        uncovered.append(area)
    uncovered.append(stations[0] - w - 1)
    uncovered.append(n - (stations[-1]+ w))
    
    answer = 0
    cover_area = 2 * w + 1
    for area in uncovered:
        if area == 0 :
            continue
        if (area % cover_area == 0):
            answer += area // cover_area 
        else:
            answer += (area // cover_area) + 1
    return answer