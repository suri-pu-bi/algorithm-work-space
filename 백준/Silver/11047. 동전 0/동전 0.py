import sys
N, K = map(int, sys.stdin.readline().split())
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

coins.sort(reverse=True)
cnt = 0
for coin in coins:
    if K == 0:
        break

    if coin > K:
        continue

    cnt += K // coin
    K -= coin * (K // coin)

print(cnt)