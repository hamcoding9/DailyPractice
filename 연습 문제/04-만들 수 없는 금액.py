N = int(input())
coin_list = list(map(int, input().split()))
coin_list.sort()

target = 1
for c in coin_list:
    if target < c:
        break
    target += c

print(target)