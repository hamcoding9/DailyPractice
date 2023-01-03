# 내 풀이
score = list(map(int, list(input())))
start = score[:len(score)//2]
end = score[len(score)//2:]
if sum(start) == sum(end):
    print("LUCKY")
else:
    print("READY")

# 다른 방식
score = input()
length = len(score)
summary = 0
for i in range(length//2):
    summary += int(score[i])
for i in range(length//2, length):
    summary -= int(score[i])
if summary == 0:
    print("LUCKY")
else:
    print("READY")