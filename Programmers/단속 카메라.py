# 내 풀이
def solution(routes):
    routes.sort(key = lambda x : x[1])
    camera = []
    is_watched = [False] * len(routes)
    for i in range(len(routes)):
        if not is_watched[i]:
            camera.append(routes[i][1])
            for j in range(i, len(routes)):
                if routes[i][1] in range(routes[j][0], routes[j][1] + 1):
                    is_watched[j] = True
    return len(camera)

# 천재같은 풀이
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer