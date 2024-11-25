'''
시간초과
- 최악의 경우 리스트 인덱스 접근 O(1) * N = O(N) 최대 M번 총 O(NM)
- 최대 100,000회의 연산을 처리해야하므로 시간 초과


import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(M):
    start, end = map(int, input().split())
    print(sum(nums[start-1:end]))

'''

import sys

def prefix_num(n):
    prefixSum[0] = nums[0]
    for i in range(1, n): # O(N)
        prefixSum[i] = prefixSum[i-1] + nums[i] # O(1)
    return prefixSum


input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
prefixSum = [0] * N
prefix_num(N)

for i in range(M): # O(M)
    start, end = map(int, input().split())
    if start == 1:
        print(prefixSum[end-1])
    else:
        print(prefixSum[end-1] - prefixSum[start-2])

# 결과 : O(N + M)