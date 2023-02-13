n = int(input())

now = 1
stack, answer = [], []

for i in range(1, n+1):
    data = int(input())
    while now <= data:
        stack.append(now)
        answer.append('+')
        now += 1
    if stack[-1] == data:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(answer))