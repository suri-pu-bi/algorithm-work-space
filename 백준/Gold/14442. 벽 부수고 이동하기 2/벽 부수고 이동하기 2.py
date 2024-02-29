import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))

visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]

visited[0][0][k] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, cnt):
    queue = deque([(x, y, cnt)])
    while queue:
        cur_x, cur_y, cnt = queue.popleft()

        if cur_x == n-1 and cur_y == m-1:
            return visited[cur_x][cur_y][cnt]

        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 다음 이동할 곳이 벽이 아니고, 아직 한번도 방문하지 않은 곳이면
                if graph[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                    visited[nx][ny][cnt] = visited[cur_x][cur_y][cnt] + 1
                    queue.append((nx, ny, cnt))

                # 다음 이동할 곳이 벽이고, 벽을 파괴한 기회가 k개 이하일 경우
                elif graph[nx][ny] == 1 and 0 < cnt <= k and visited[nx][ny][cnt-1] == 0 :
                    visited[nx][ny][cnt-1] = visited[cur_x][cur_y][cnt] + 1
                    queue.append((nx, ny, cnt-1))

    return -1

print(bfs(0, 0, k))