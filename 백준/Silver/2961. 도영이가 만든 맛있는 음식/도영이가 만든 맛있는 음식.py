import sys
from itertools import combinations
n = int(sys.stdin.readline())

minValue = 0
sour = []
bitter = []


for _ in range(n):
    t1, t2 = map(int,sys.stdin.readline().split())
    sour.append(t1)
    bitter.append(t2)

answer = 1e9 # 매우 큰 숫자(10억)로 초기화

for i in range(1, n+1):
    combiIdx = list(combinations(list(range(n)), i)) # combination index

    for food in combiIdx: # [(0,1), (0,2) ...]
        # i=2 재료를 2개 선택한 상황이고, 첫번째 for문에서 (0,1)이 선택된 상태라면,

        # 초기화
        s = 1
        b = 0

        # 신맛, 쓴맛 계산
        for j in range(i): # i=len(food), (0,1) = 0번째, 1번째 재료를 뽑은 것
            # 신맛 리스트에서 0번째, 1번째 재료를 곱하기
            # 쓴맛 리스트에서 0번쨰, 1번째 재료를 더하기
            s *= sour[food[j]]
            b += bitter[food[j]]

        answer = min(answer, abs(s-b))


print(answer)