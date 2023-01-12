n, c = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
array.sort()

start, end = 1, array[-1] - array[0]
gap = 0
while start <= end:
    mid = (start + end) // 2
    count = 1
    installed = array[0]
    for i in range(1, n):
        if array[i] >= installed + mid:
            installed = array[i]
            count += 1
    if count >= c:
        gap = mid
        start = mid + 1
    else:
        end = mid -1

print(gap)