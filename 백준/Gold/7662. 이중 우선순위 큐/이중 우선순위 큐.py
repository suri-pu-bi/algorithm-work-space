import heapq
import sys

def isEmpty(nums):
    for item in nums:
        if item[1] > 0: # {키: 값} , item[0] = 키, item[1] = 값 의미
            return False
    return True

t = int(sys.stdin.readline())

for _ in range(t):
    min_heap = []
    max_heap = []
    nums = dict() # 값의 추가, 삭제를 공통적으로 기록하고 공유하는 공간
    k = int(sys.stdin.readline())

    for _ in range(k):
        ch, n = sys.stdin.readline().strip().split()
        n = int(n)

        # 문자가 I일 때 삽입
        if ch =='I':
            # 중복 삽입일 경우
            if n in nums:
                nums[n] += 1 # 개수만 하나 추가

            # 최초 삽입일 경우
            else:
                nums[n] = 1
                # 최소 힙
                heapq.heappush(min_heap, n)
                # 최대 힙
                heapq.heappush(max_heap, -n)

        # 문자가 D일 때 삭제
        elif ch == 'D':
            # 큐에 원소가 있다면 삭제 작업
            if not isEmpty(nums.items()):
                # 최댓값을 제거
                if n == 1:
                    # head에 있는 데이터가 nums에 존재하지 않거나 nums에 값이 0인 상태로 존재하면,
                    # 실제로 삭제되었지만, 반영되지 않은 데이터
                    while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
                        temp = -heapq.heappop(max_heap) # 힙에서 제거
                        if temp in nums: # nums에도 남아있다면
                            del(nums[temp]) # 삭제

                    # nums 갱신
                    nums[-max_heap[0]] -= 1


                # 최소값을 제거
                else:
                    while min_heap[0] not in nums or nums[min_heap[0]] < 1:
                        temp = heapq.heappop(min_heap)
                        if temp in nums:
                            del(nums[temp])

                    # nums 갱신
                    nums[min_heap[0]] -= 1

    # 모든 연산 처리 후, 큐가 비어있으면 'EMPTY' 출력
    if isEmpty(nums.items()):
        print('EMPTY')

    # 모든 연산 처리 후, 큐가 비어있지 않을 때 최대값과 최솟값 출력
    else:
        # 최소 힙과 최대힙에서 삭제되었지만 남아있는 데이터를 삭제한 후 head 데티어 출력하기
        while min_heap[0] not in nums or nums[min_heap[0]] < 1:
            heapq.heappop(min_heap)

        while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
            heapq.heappop(max_heap)

        print(-max_heap[0], min_heap[0])

