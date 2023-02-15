from collections import deque

n, k = map(int, input().split())
belt = list(map(int, input().split()))
robot = [False] * n

belt, robot = deque(belt), deque(robot)
count = 1

while True:
    belt.rotate()
    robot.rotate()
    if robot[n - 1] == True:
        robot[n - 1] = False
    for i in range(n - 2, -1, -1):
        if robot[i] == True and belt[i + 1] >= 1 and robot[i + 1] == False:
            robot[i] = False
            robot[i + 1] = True
            belt[i + 1] -= 1
    if robot[n - 1] == True:
        robot[n - 1] = False
    if belt[0] >= 1:
        robot[0] = True
        belt[0] -= 1
    if belt.count(0) >= k:
        break
    count += 1

print(count)