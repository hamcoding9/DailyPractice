# 사용할 수 있는 기능: enumerate?
def solution(s):
    answer = ''
    words = s.split(' ')
    for word in words:
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '
        
    return answer

answer = solution('try hello world')
print(answer)