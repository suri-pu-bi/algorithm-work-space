import sys

n, m = map(int, sys.stdin.readline().strip().split())
trees = list(map(int, sys.stdin.readline().strip().split()))

start = 0
end = max(trees) # trees[-1]

while start <= end:

    mid = (start + end) // 2
    cnt = 0

    for i in trees:
        if mid <= i:
            cnt += i - mid

    if cnt >= m:
        start = mid + 1

    else:
        end = mid - 1

print(end)

