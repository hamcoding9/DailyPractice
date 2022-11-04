# 효율성 테스트: 0점
# 기지국이 커버하지 못하는 위치를 저장하는 방식이 O(N)이라서 그런 것 같다 ...
def solution(n, stations, w):
    graph = [0] * (n + 1)
    # 기지국이 커버하는 위치를 표시한다
    for apt in stations:
        left = max(1, apt - w)
        right = min(apt + w, n)
        graph[left:right + 1] = [1] * (right - left + 1)
    print(graph)
    # 기지국이 커버하지 못하는 위치를 저장한다
    uncovered = []
    count = 0
    for i in range(1, len(graph) + 1) :
        if i == len(graph):
            if count > 0:
                uncovered.append(count)
            break   
        if graph[i] == 1:
            if count > 0:
                uncovered.append(count)
            count = 0
            continue
        if graph[i] == 0:
            count += 1
    print(uncovered)
    # 추가로 필요한 기지국의 개수를 계산한다
    answer = 0
    cover_area = 2 * w + 1
    for num in uncovered:
        if (num % cover_area == 0):
            answer += num // cover_area
        else:
            answer += (num // cover_area) + 1
    return answer