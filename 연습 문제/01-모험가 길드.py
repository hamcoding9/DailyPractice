N = int(input())
people_list = list(map(int, input().split()))

people_list.sort()
answer = 0
count = 0

for i in people_list:
    count += 1
    if i <= count:
        answer += 1
        count = 0

print(answer)