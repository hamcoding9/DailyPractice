# 현상황: 시간 초과
from collections import OrderedDict

n, m = map(int,input().split())
ovenlist= list(map(int, input().split()))
pizzas = list(map(int, input().split()))

oven = OrderedDict()
for i in range(n):
    oven[i+1] = ovenlist[i]

pizza_index = [] # 피자가 차례로 들어간 오븐의 위치를 담는 리스트
while oven: # 오븐을 다 순회할 때까지
    if len(pizzas)==0: break
    items = oven.popitem()
    if pizzas[0] < items[1]: # 피자가 들어가는 경우
        pizza_index.append(items[0]) # 오븐의 위치 넣기
        del pizzas[0]
    else: # 피자가 들어가지 않는 경우
        continue

# 피자가 모두 들어간 경우
if len(pizza_index) == m:
    print(pizza_index[-1])
else: # 피자가 모두 들어가지 않은 경우
    print(0)