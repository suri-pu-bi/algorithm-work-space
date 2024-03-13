import sys
import heapq

n = int(sys.stdin.readline())
problems = []
for _ in range(n):
    problems.append(tuple(map(int, sys.stdin.readline().split())))

problems.sort()

queue = []

for i in problems:
    heapq.heappush(queue, i[1])
    if i[0] < len(queue):
        heapq.heappop(queue)

print(sum(queue))