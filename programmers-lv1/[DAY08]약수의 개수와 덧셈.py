# 첫 번째 시도
def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        if (len([i for i in range(1,(n//2+1)) if n%i==0]) % 2) == 0 :
            answer -= n
        else: 
            answer += n
    return answer
  
# 다른 분 코드1: 제곱수는 약수의 개수가 홀수이므로 이 사실을 이용
def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        if int(n**0.5) == n**0.5:
            answer -= n
        else:
            answer += n
    return answer
  
# 다른 분 코드2: 약수의 개수가 홀수이면 -, 짝수이면 + => (-1)의 제곱을 이용
def solution(left, right):
    return sum([pow(-1, len([i for i in range(1, n//2+1) if n%i==0])+1)*n for n in range(left, right+1)])
