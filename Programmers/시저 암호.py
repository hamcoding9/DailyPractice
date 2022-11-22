def solution(s, n):
    keys = ['abcdefghijklmopqrstuwxyz', 'ABCDEFGHIJKLMOPQRSTUWXYZ', ' ']
    answer = ''
    for letter in s:
        if letter.islower():
            answer += keys[0][((keys[0].index(letter))+n)%24]
        elif letter.isupper():
            answer += keys[1][((keys[1].index(letter))+n)%24]
        else:
            answer += keys[2]
    return answer

print(solution('Z  Zz  zZZ Z', 5))