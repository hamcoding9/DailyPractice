n = int(input())
score = []
for i in range(n):
    student = list(input().split())
    score.append(student)

sorted_score = sorted(score, key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in sorted_score:
    print(student[0])
