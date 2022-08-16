def solution(n):
    answer = ''
    letter = '수박'
    for i in range(n):
        answer += letter[i%2]
    return answer