import sys

# 행복한 유치원 문제와 비슷

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
sensor = list(map(int, sys.stdin.readline().split()))
sensor.sort()

distance = []
for i in range(n-1):
    distance.append(sensor[i+1] - sensor[i])

distance.sort()
print(sum(distance[:n-m]))

