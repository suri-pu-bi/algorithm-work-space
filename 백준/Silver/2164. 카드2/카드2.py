import sys
from collections import deque
n = int(sys.stdin.readline())

cards = deque([i+1 for i in range(n)])

while len(cards) > 1:
    cards.popleft()
    temp = cards.popleft()
    cards.append(temp)

print(cards[0])