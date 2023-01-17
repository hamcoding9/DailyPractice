import heapq

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))

answer = 0

while len(cards) > 1:
    card = heapq.heappop(cards) + heapq.heappop(cards)
    answer += card
    heapq.heappush(cards, card)

print(answer)