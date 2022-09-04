# DailyPractice

This reprository contains codes designed to prepare for the coding interview. README.md also contains my personal wiki that summarizes the knowledge I gained while studying.

## Challenge1(in progess)

* **Solving at least one problem every day for 100 days**

* start date: 2022.08.12
* progress     ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/19)

# Personal Wiki

* [정규 표현식](#정규-표현식)
* [리스트](#리스트)

---

### 정규 표현식

- `re.sub()` : 문자열 치환하기

  ```python 
  s = re.sub('[^0-9a-zA-Z]','',s)
  ```

---
### 리스트

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
