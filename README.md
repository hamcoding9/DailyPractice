# DailyPractice

This reprository contains codes designed to prepare for the coding interview. README.md also contains my personal wiki that summarizes the knowledge I gained while studying.

## Challenge1(in progess)

* **Solving at least one problem every day for 100 days**

* start date: 2022.08.12
* progress     ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/36)

# Personal Wiki

* [정규 표현식](#정규-표현식)
* [리스트](#리스트)
* [딕셔너리](#딕셔너리)
* [기타](#기타)
  * [아스키 코드](#아스키-코드)
---

## 정규 표현식

- `re.sub()` : 문자열 치환하기

  ```python 
  s = re.sub('[^0-9a-zA-Z]','',s)
  ```

---
## 리스트

* 리스트 복사하기(shallow copy)

```python
a = [1, 2, 3]
b = a[:]
```

* 리스트 뒤집기

```python
a = [1, 2, 3]
a.reverse()
```

* 중첩 리스트에서 max값, min값 찾기
```python
l = [[6, 8, 2, 6, 2], [3, 2, 3, 4, 6], [6, 7, 3, 3, 2]]
max_int = max(map(max, l))
```

---
## 딕셔너리

* 딕셔너리 정렬
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

* 딕셔너리의 get() 함수
```python
# get(x, 디폴트 값) : 딕셔너리 안에 찾으려는 key 값이 없을 경우 디폴트 값을 return함
d['f'] = d.get('f', 0)
d
# {'a': 1, 'b': 1, 'e': 1, 'c': 0, 'f': 0}
```

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
