# 1. 2022-10-17에 푼 코드
# 2. OrderedDict를 활용
# 3. 오븐 길이를 전부 순회하므로 O(n)으로 시간 초과가 나옴

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
    
# 1. 2022-10-18에 푼 코드

n, m = map(int,input().split())
oven = list(map(int, input().split()))
pizzas = list(map(int, input().split()))

for i in range(n-1):
    if oven[i] < oven[i+1]:
        oven[i+1] = oven[i]
        
p = 0        
for i in range(n - 1, -1, -1):
    if pizzas[p] > oven[i]:
        continue
    p += 1
    if p == m:
        print(i+1)
        break

if p < m:
    print(0)