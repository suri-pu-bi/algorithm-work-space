import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    raw = list(map(int, list(sys.stdin.readline().rstrip())))
    graph.append(raw)

# 중간에 벽을 단 한번만 부술 수 있으므로 벽을 부쉈는지 여부를 3차원 행렬로 표현
# z가 0이면 벽을 파괴할 수 있고, z가 1이면 불가능
# 벽을 부수지 않은 경로, 벽을 부순 경로
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

# 처음 시작 노드 포함이므로 벽을 부수지않은 경로에 개수 1로 설정
visited[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최단경로 -> bfs
def bfs(x, y, z):
    queue = deque([(x, y, 0)])

    while queue:
        cur_x, cur_y, cnt = queue.popleft()

        # 끝 점에 도달하면 이동 횟수를 출력
        if cur_x == n-1 and cur_y == m-1 :
            return visited[cur_x][cur_y][cnt]

        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 다음 이동할 곳이 벽이 아니고, 아직 한번도 방문하지 않은 곳이면
                # 벽 파괴기회를 한번 사용하면 계속 cnt는 1 (index가 1인 곳에 계속 개수 저장)
                if graph[nx][ny] == 0 and visited[nx][ny][cnt] == 0 :
                    visited[nx][ny][cnt] = visited[cur_x][cur_y][cnt] + 1
                    queue.append((nx, ny, cnt))

                # 다음 이동할 곳이 벽이고, 벽 파괴기회를 사용하지 않은 경우
                elif graph[nx][ny] == 1 and cnt == 0 :
                    # 벽을 부순 경로에 개수 추가
                    visited[nx][ny][1] = visited[cur_x][cur_y][0] + 1
                    queue.append((nx, ny, 1))

    return -1


print(bfs(0, 0, 0))