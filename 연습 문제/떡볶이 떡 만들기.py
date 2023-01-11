# 파라메트릭 서치 문제
n, m = map(int, input().split())
t_list = list(map(int, input().split()))

t_list.sort()
start, end = 0, t_list[-1]

while start <= end:
    mid = (start + end) // 2
    total_length = 0
    for t in t_list:
        if t > mid:
            total_length += (t - mid)
    if total_length >= m:
        start = mid + 1
        cutter = mid
    else:
        end = mid - 1

print(cutter)