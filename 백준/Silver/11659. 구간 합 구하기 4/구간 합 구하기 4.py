import sys

def prefix_num(n):
    prefixSum[0] = nums[0]
    for i in range(1, n):
        prefixSum[i] = prefixSum[i-1] + nums[i]
    return prefixSum


input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
prefixSum = [0] * N
prefix_num(N)

for i in range(M):
    start, end = map(int, input().split())
    if start == 1:
        print(prefixSum[end-1])
    else:
        print(prefixSum[end-1] - prefixSum[start-2])