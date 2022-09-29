# 방법1: 해시로 풀기
n = int(input())
mycard = map(int, input().split())
m = int(input())
qcard = map(int, input().split())

hash = {}
for card in mycard:
    hash[card] = hash.get(card, 1)
answer = []
for card in qcard:
    if card not in hash:
        print('0', end=' ')
    else:
        print('1', end=' ')

# 방법2: 이진탐색으로 풀기
n = int(input())
mycard = list(map(int, input().split()))
m = int(input())
qcard = list(map(int, input().split()))

mycard.sort()

def binary_search(target):
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if mycard[mid] == target:
            return 1
        elif mycard[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for card in qcard:
    print(binary_search(card), end = ' ')
