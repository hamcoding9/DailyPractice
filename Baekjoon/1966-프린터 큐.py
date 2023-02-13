from collections import deque

answer = []

repeat = int(input())

for i in range(repeat):
    count = 0
    queue = deque()
    n, m = map(int, input().split())
    rank = list(map(int, input().split()))
    for i in range(n):
        queue.append((i, rank[i]))

    while queue:
        is_small = False
        for i in range(1, len(queue)):
            if queue[0][1] < queue[i][1]:
                is_small = True
                break
        if is_small:
            a = queue.popleft()
            queue.append(a)
        else:    
            a = queue.popleft()
            count += 1
            if a[0] == m:
                answer.append(count)

for x in answer:
    print(x)

# 더 파이썬스럽게

test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    queue = [(i, idx) for idx, i in enumerate(queue)]

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x:x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))