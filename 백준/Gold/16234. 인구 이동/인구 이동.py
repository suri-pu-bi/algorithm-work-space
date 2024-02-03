import sys
from collections import deque

N, L, R = map(int,sys.stdin.readline().split())
countries = []
for _ in range(N):
    countries.append(list(map(int, sys.stdin.readline().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x,y):
    # 전역에 visited 선언 -> 여기서 선언안해도됨
    queue = deque()
    idx_list = []
    queue.append((x, y))
    idx_list.append((x, y))

    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(countries[cur_x][cur_y] - countries[nx][ny]) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    idx_list.append((nx, ny))

    return idx_list


answer = 0
while True:
    visited = [[0] * (N) for _ in range(N)]
    flag = False

    for i in range(N):
        for j in range(N):
            # 유기농 배추처럼 부분 집단이 몇개씩 나올 수 있으므로 하나씩 bfs 해줘야함
            if visited[i][j] == 0:
                visited[i][j] = 1

                groups = bfs(i, j)
                groups_length = len(groups)

                # 국가 하나만 나오면 연합이 안된 것
                if groups_length > 1:
                    flag = True
                    people_cnt = sum([countries[x][y] for x, y in groups]) // groups_length

                    for x, y in groups:
                        countries[x][y] = people_cnt

    # 반복문을 다 돌렸는데 flag가 False이면 더이상 인구이동 불가능
    if not flag:
        break

    answer += 1

print(answer)