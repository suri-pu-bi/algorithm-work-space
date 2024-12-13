import sys
n = int(sys.stdin.readline())

dp = [0 for _ in range(1001)]


dp[1] = 1
dp[2] = 3

# dp[i-2]가 dp[i]에서 두 번 들어갈 수 있기 때문에 *2 
for i in range(3, 1001):
    dp[i] = (2 * dp[i-2] + dp[i-1]) % 10007

print(dp[n])