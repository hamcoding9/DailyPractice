# 첫 번째 시도, 테스트케이스 11 통과 X
def solution(numbers):
    temp = sorted([str(i) for i in numbers], key=lambda x: (x*4)[:4], reverse=True)
    answer = ''.join(temp)
    return answer

# 두 번째 시도
# 제한 사항을 유심히 보자!
def solution(numbers):
    numbers = sorted([str(i) for i in numbers], key=lambda x: (x*4)[:4], reverse=True)
    answer = '0' if numbers[0]=='0' else ''.join(numbers)
    return answer