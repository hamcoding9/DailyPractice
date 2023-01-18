input = input()

input = "0" + input
acc = 0

for i in range(1, len(input)):
    num = int(input[i])
    pre = int(input[i-1])
    if pre <= 1 or acc <= 1:
        acc += num
    else:
        acc *= num
    
print(acc)