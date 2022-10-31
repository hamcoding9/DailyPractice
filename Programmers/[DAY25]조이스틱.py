def solution(name):
    answer = 0
    # A-Z 알파벳 이동(고정)
    jump = [min(ord(x)-ord('A'),ord('Z')-ord(x)+1) for x in name]
    ptr = 0
    while True:
        answer += jump[ptr]
        # 이동 완료했으므로 0 부여
        jump[ptr] = 0
        if sum(jump) == 0: break
        left, right = 1, 1
        # 0이 등장할 때까지 left, right를 이동
        while jump[ptr-left] == 0:
            left += 1
        while jump[ptr+right] == 0:
            right += 1
        # 현재 위치에서 더 가까운 것을 선택(greedy)
        if left >= right:
            ptr += right
            answer += right
        else:
            ptr -= left
            answer += left
    return answer