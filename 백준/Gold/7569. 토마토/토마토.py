import sys
from collections import deque

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

def bfs():
    while queue:
        # 배열 인덱스 조심
        z, x, y = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = tomato[z][x][y] + 1 
                queue.append([nz, nx, ny])



m, n, h = map(int, sys.stdin.readline().split())
tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
queue = deque()
day = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append([i, j, k])

bfs()

for box in tomato :
    for row in box:
        if 0 in row:
            print(-1)
            exit() # break문은 반복문 하나만 빠져나감

        day = max(day, max(row))

print(day - 1)