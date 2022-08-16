# 첫 번째 방법
def solution(strings, n):
    strings.sort()
    keys = sorted([(word[n], idx) for idx, word in enumerate(strings)])
    return [strings[keys[i][1]] for i in range(len(keys))]
  
# 두 번째 방법 (sorted 함수의 key 활용)
def solution(strings, n):
    strings.sort()
    return sorted(strings, key=lambda x:x[n])
