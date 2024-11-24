import sys
n = int(sys.stdin.readline())

dp = [0 for _ in range(1001)]
dp[1] = 1
dp[2] = 2

# 분배법칙에 의해 중간과정에서 나머지를 계산하는 것과 최종 정답에서 나머지를 계산하는 것은 동일
# 너무 큰 수가 돼서 오버플로우가 되지않게 하려고 중간과정에서 계산
for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 10007

print(dp[n])