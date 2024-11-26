import sys
from collections import deque


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # 0인 것은 큐에 넣으면 안됨
                if graph[nx][ny] == 1:
                    graph_copy[nx][ny] = graph_copy[x][y] + 1
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
graph_copy = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)
            break

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1: # -1 출력
            print(-1, end=" ")
        else:
            print(graph_copy[i][j], end=" ")
    print()
