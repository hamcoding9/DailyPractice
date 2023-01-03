string = input()
alpha, digit = [], 0
for s in string:
    if s.isdigit():
        digit += int(s)
    else:
        alpha.append(s)
alpha.sort()
if digit != 0:
    alpha.append(str(digit))
answer = ''.join(alpha)
print(answer)