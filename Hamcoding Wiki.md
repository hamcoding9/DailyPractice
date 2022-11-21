# Hamcoding Wiki

* [문자열](#문자열)
* [리스트](#리스트)
* [딕셔너리](#딕셔너리)
* [힙](#힙)
* [데크](#힙)
* [기타](#기타)
  * [아스키 코드](#아스키-코드)
  * [조합](#조합)
  * [10진수](#10진수)
  * [팩토리얼](#팩토리얼)
  * [정규 표현식](#정규-표현식)
---

## 문자열

### 공백 제거

```python
string = "   a  bc  "
# 모든 공백 제거
result = string.replace(" ", "")
# 양측 공백 제거
result_s = string.strip()
# 좌측 공백 제거
result_ls = string.lstrip()
# 우측 공백 제거
result_rs = string.rstrip()
```



## 리스트

### 리스트 복사하기

```python
# shallow copy
a = [1, 2, 3]
b = a
# deep copy
from copy import deepcopy
c = deepcopy(a)
```

### 리스트 뒤집기

```python
a = [1, 2, 3]
a.reverse()
```

### 중첩 리스트에서 max값, min값 찾기

```python
l = [[6, 8, 2, 6, 2], [3, 2, 3, 4, 6], [6, 7, 3, 3, 2]]
max_int = max(map(max, l))
```

---
[목차](#Hamcoding-Wiki)

## 딕셔너리

### 딕셔너리 정렬

```python
d = {'a':1, 'b':1, 'e':1, 'c':0}

# 딕셔너리 key를 기준으로 정렬
sorted(d.items())
# [('a', 1), ('b', 1), ('c', 0), ('e', 1)]

# 딕셔너리 key 정렬 후 key만 보기
sorted(d)
# ['a', 'b', 'c', 'e']

# 딕셔너리 value를 기준으로 정렬
sorted(d.items(), key=lambda x: x[1])
# [('c', 0), ('a', 1), ('b', 1), ('e', 1)]
```

### 딕셔너리의 get() 함수

```python
# get(x, 디폴트 값) : 딕셔너리 안에 찾으려는 key 값이 없을 경우 디폴트 값을 return함
d['f'] = d.get('f', 0)
d
# {'a': 1, 'b': 1, 'e': 1, 'c': 0, 'f': 0}
```

[목차](#Hamcoding-Wiki)

## 힙

* 새로운 자료가 추가될 때마다 정렬해야 하는 경우, 사용하기!
* 매번 최솟값/최댓값을 꺼내야 하는 알고리즘에서 사용

### 기본 사용법

```python
import heapq
# 힙 생성 및 원소 추가
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 50)
# 이미 있는 리스트로 힙 생성하는 방법
heap = [10, 20, 50]
heapq.heapify(heap)
# 힙에서 원소 꺼내기
min_value = heapq.heappop(heap)
# 원소를 삭제하지 않고 min 꺼내기
min_value = heap[0]
```

### max heap 만들기

* (-1)를 곱하는 트릭을 사용한다.

```python
heap_items = [1, 3, 5, 7, 9]
max_heap = []
for item in heap_items:
    heapq.heappush(max_heap, (-item, item))
max_item = heapq.heappop(max_heap)[1]
```

[목차](#Hamcoding-Wiki)

## 데크

* push/pop 연산이 빈번한 알고리즘에서 사용
* 시작점의 값을 넣고 빼거나 끝점의 값을 넣고 뺄 때 최적화된 연산 속도 O(1)을 제공한다.

```python
from collections import deque
l = [1, 2, 3]
deq = deque(l)
deq.appendleft(0) 
# deque([0, 1, 2, 3])
deq.append(4)
# deque([0, 1, 2, 3, 4])
deq.popleft()
# 0
# deque([1, 2, 3, 4])
deq.pop()
# 4
# deque([1, 2, 3])
deq.rotate(1)
# deque([3, 1, 2])
```

[목차](#Hamcoding-Wiki)

## 기타

### 아스키 코드


`ord()` : 문자 -> 아스키 코드


`chr()` : 아스키 코드 -> 문자


```python
ord('A')
# 65
chr(65)
# 'A'
```

### 순열과 조합
```python
from itertools import combinations
from itertools import permutations
items = [1, 2, 3, 4, 5]
list(combinations(items, 3))
list(permutations(items, 3))
```

### 10진수

```python
value = 7

b = bin(value)
o = oct(value)
h = hex(value)

print(b) # 0b111
print(o) # 0o7
print(h) # 0x7
```

### 팩토리얼

```python
from math import factorial
print(factorial(3)) # 6
```

[목차](#Hamcoding-Wiki)

### 정규 표현식

- `re.sub()` : 문자열 치환하기

  ```python 
  s = re.sub('[^0-9a-zA-Z]','',s)
  ```

