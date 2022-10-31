def solution(s):
    return ''.join(sorted([i for i in s],reverse=True))
  
# 더 간결(sorted 함수의 성질)
def solution(s):
    return ''.join(sorted(s ,reverse=True))
