import sys
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                # 몇 번째날 해당 토마토가 익었는지 알기 위해 이전좌표에 +1을 해줌
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx, ny])


M, N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            # 토마토가 모두 익는 최소날짜를 구해야하므로 익은 토마토의 위치를 모두 큐에 넣어놓아야함
            queue.append([i, j])

# 토마토 익히기 시작
bfs()

day = 0
for row in tomato:
    if 0 in row:
    # 익지 않은 토마토가 있으면(=토마토가 모두 익지 못하는 상황) -1 출력
        print(-1)
        exit() # 다음 행의 여부와 관계없이 종료시킴
    # 토마토가 모두 익은 상황이라면, 모든 토마토 중 가장 마지막에 익은 토마토의 날짜를 찾아야함
    # 즉, 각 행마다 최댓값들을 찾아 큰 값으로 갱신해야함
    day = max(day, max(row))

# BFS에서 처음 시작을 0이 아닌 1부터 했으므로 -1을 해야 날짜를 구할 수 있음
print(day - 1)