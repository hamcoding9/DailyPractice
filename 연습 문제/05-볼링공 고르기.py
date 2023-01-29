n, m = map(int, input().split())
balls = list(map(int, input().split()))

balls.sort()
count = 0

for i in range(len(balls) - 1):
    selected = balls[i]
    for ball in balls[i+1:]:
        if selected != ball:
            count += 1

print(count)