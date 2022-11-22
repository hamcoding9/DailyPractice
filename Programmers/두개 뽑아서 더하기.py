def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(1, len(numbers) - i):
            num = numbers[i] + numbers[i + j]
            if num not in answer:
                answer.append(num)
    answer.sort()
    return answer

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    return sorted(list(set(answer)))