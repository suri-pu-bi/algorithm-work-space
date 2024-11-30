import sys
input = sys.stdin.readline
N = int(input())
dots = []
for _ in range(N):
    x, y = map(int, input().split())
    dots.append((x, y))

dots.sort(key= lambda x : (x[0], x[1]))

for i in range(N):
    for j in range(2):
        print(dots[i][j], end=" ")
    print()
