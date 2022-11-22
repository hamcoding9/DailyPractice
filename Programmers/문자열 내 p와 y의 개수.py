# 첫 번째
def solution(s):
    letter1 = s.count('y') + s.count('Y')
    letter2 = s.count('p') + s.count('P')
    if letter1 == letter2 & letter1 > 0:
        return True
    else:
        return False
    
# 두 번째
def solution(s):
    if s.lower().count('y') == s.lower().count('p'):
        return True
    else:
        return False
    
# -> 더 줄이기
def solution(s):
    return s.lower().count('y') == s.lower().count('p')