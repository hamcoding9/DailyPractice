def solution(people, limit):
    people.sort()
    start, end = 0, len(people) - 1
    count = 0 # 두 명이서 같이 탈 수 있는 경우
    while start < end:
        if people[start] + people[end] <= limit:
            start += 1
            count += 1
        end -= 1
    return len(people) - count
