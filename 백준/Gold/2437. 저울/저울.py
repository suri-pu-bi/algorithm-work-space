import sys
n = int(sys.stdin.readline())
weight = (list(map(int, sys.stdin.readline().split())))
weight.sort()

target = 1
for i in weight:
    if target < i:
        break
    target += i

print(target)

