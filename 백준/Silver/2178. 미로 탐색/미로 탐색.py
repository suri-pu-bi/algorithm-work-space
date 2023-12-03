import sys
from collections import deque

# 최단 경로를 찾는 문제
def bfs(start, end):
    queue = deque([(start,end)])
    visited = [[0] * m for _ in range(n)]
    visited[start][end] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    # 1일 때만 상하좌우로 이동할 수 있기 때문에
                    # 1 (14) -> 오른쪽 1 (15), 아래쪽 1 (15) 이런식으로
                    # 최소 칸 수를 더해줌
                    maze[nx][ny] = maze[x][y] + 1
    # print(maze)
    return maze[n-1][m-1]


n, m = map(int, sys.stdin.readline().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, list(sys.stdin.readline().strip()))))

print(bfs(0,0))

