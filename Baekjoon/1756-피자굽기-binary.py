n, m = map(int,input().split())
oven = list(map(int, input().split()))
pizzas = list(map(int, input().split()))

for i in range(n-1):
    if oven[i] < oven[i+1]:
        oven[i+1] = oven[i]
        
def binary_search(start:int, end:int, target:int) -> int:
    # 종료 조건
    if start > end: return -1
    # start와 end가 한칸 차이 나는 경우 종료
    if end - start == 1:
        if oven[start] >= target: # 도우가 오븐에 들어가면
            return start
        else: # 들어가지 않는 경우
            return -1

    mid = (start + end) // 2
    if oven[mid] >= target: # 도우가 오븐에 들어가면
        return binary_search(mid, end, target)
    else:
        return binary_search(start, mid, target)

# 오븐 순회
start, end = 0, n
for p in pizzas:
    end = binary_search(start, end, p)
    
print(end + 1)