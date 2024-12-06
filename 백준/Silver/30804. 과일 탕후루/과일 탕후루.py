'''시간초과 해결
- 포인터를 두 개 다 왼쪽을 시작으로 두면서, 오른쪽 포인터를 오른쪽으로 계속 이동
- 왼쪽 포인터를 종류가 2개가 될 때까지 오른쪽으로 이동
- 종류 개수 판별을 배열에서 set으로 변환시키는 대신 dictionary 사용
'''

from collections import defaultdict
import sys
def max_fruit_tanghulu_length(N, fruits):
    left = 0
    right = 0
    fruit_count = defaultdict(int)
    max_length = 0

    while right < N:
        # 오른쪽 포인터가 가리키는 과일 추가
        fruit_count[fruits[right]] += 1

        # 과일 종류가 2개를 초과하면 왼쪽 포인터 이동
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1 # 오른쪽 포인터가 이미 추가한 과일
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1

        # 현재 상태에서 최대 길이 갱신
        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length


N = int(sys.stdin.readline())
fruits = list(map(int, sys.stdin.readline().split()))

print(max_fruit_tanghulu_length(N, fruits))