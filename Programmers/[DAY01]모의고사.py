def solution(answers):
    s1 = [1, 2, 3, 4, 5] # 수포자1. 5 주기로 반복
    s2 = [2, 1, 2, 3, 2, 4, 2, 5] # 수포자2. 8 주기로 반복
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 수포자 3. 10 주기로 반복
    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == s1[i%5]:
            cnt[0] += 1
        if answers[i] == s2[i%8]:
            cnt[1] += 1
        if answers[i] == s3[i%10]:
            cnt[2] += 1
    max_cnt = max(cnt)
    answer = []
    for i in range(3):
        if max_cnt == cnt[i]:
            answer.append(i+1)
            
    return answer

answers = [1, 2, 3, 4, 5, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
answer = solution(answers)
print(answer)