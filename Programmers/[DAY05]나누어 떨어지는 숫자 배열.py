# 첫 번째 방법

def solution(arr, divisor):
    answer = [i for i in arr if i%divisor==0]
    if len(answer) == 0: answer.append(-1)
    answer.sort()
    return answer

# 두 번째 방법
def solution(arr, divisor):
    return sorted([i for i in arr if i%divisor==0]) or [-1]
