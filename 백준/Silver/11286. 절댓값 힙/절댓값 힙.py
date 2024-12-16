import sys
import heapq
N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x != 0:
        # (절댓값이 가장 작은 값, 숫자가 가장 작은 값) 튜플로 힙에 넣기
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else: # 힙이 비어있는 경우, 0 출력
            print(0)
