from sys import stdin
import heapq

heap = []
x = 0
N = int(stdin.readline())
for i in range(N):
    x = int(stdin.readline())
    if x > 0: # 자연수일 경우 
        heapq.heappush(heap, -x)
    elif x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-(heapq.heappop(heap)))