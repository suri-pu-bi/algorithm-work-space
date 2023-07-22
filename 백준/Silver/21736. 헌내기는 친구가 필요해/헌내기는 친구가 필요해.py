import sys
from collections import deque


def bfs(i, j):
    cnt = 0
    queue = deque([(i, j)])
    visited = [[0]*m for _ in range(n)]
    visited[i][j] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            x_cur = x + dx[i]
            y_cur = y + dy[i]

            if 0 <= x_cur < n and 0 <= y_cur < m:
                if campus[x_cur][y_cur] != 'X' and visited[x_cur][y_cur] == 0:
                    queue.append((x_cur, y_cur))
                    visited[x_cur][y_cur] = 1

                    if campus[x_cur][y_cur] == 'P':
                        cnt += 1
    if cnt != 0:
        return cnt

    else:
        return "TT"


n, m = map(int, sys.stdin.readline().split())
campus = []
for i in range(n):
        campus.append(list(sys.stdin.readline().strip()))


for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            print(bfs(i, j))