# 처음 푼 코드
# 10번 시간 초과, 12번 런타임 에러
def solution(number, k):
    nums, answer = [i for i in number], []
    while k:
        max_item, max_idx = nums[0], 0
        for i in range(k+1):
            if nums[i] > max_item:
                max_item = nums[i]
                max_idx = i
        answer.append(max_item)
        nums = nums[max_idx+1:]
        k -= max_idx
    answer+= nums
    return ''.join(answer)

# 강의 보고 수정한 코드
def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
        
    collected = collected[:-k] if k > 0 else collected
    answer = ''.join(collected)
    return answer