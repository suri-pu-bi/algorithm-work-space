import sys
from collections import deque

# readlline 뒤에 괄호를 넣으면 에러가 생김 조심!
input = sys.stdin.readline
n = int(input())
space = []

# 상어의 위치와 크기
shark_x, shark_y, shark_size = 0, 0, 2

for i in range(n):
    space.append(list(map(int, input().split())))
    for j in range(n):
        if space[i][j] == 9:
            shark_x = i
            shark_y = j

# 상하좌우
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def eat_fish(x, y, shark_size):
    visited = [[0] * n for _ in range(n)]
    # 이동한 거리
    distance = [[0] * n for _ in range(n)]

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    # 식사 리스트
    fishes = []

    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # 이동할 수 있다면
                if space[nx][ny] <= shark_size:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cur_x][cur_y] + 1

                    if space[nx][ny] < shark_size and space[nx][ny] != 0:
                        fishes.append((nx, ny, distance[nx][ny]))

    # 우선순위 : 거리가 가까운 물고기 > 가장 위에 있는 물고기 > 가장 왼쪽에 있는 물고기
    # 내림차순으로 정렬해야 pop 했을 때 가장 뒤에 있는 값이 가장 적합한 fish!
    return sorted(fishes, key=lambda x: (-x[2], -x[0], -x[1]))


time = 0
count = 0
while True:
    eatable_fishes = eat_fish(shark_x, shark_y, shark_size)

    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 엄마상어에게 도움 요청
    if len(eatable_fishes) == 0:
        break

    # 먹을 물고기 pick <- 이미 정렬된 상태
    nx, ny, dist = eatable_fishes.pop()

    # 움직이는 칸 수 = 시간
    time += dist

    # 상어가 있었던 위치와 먹은 물고기가 있었던 위치를 0으로 만들기
    space[shark_x][shark_y], space[nx][ny] = 0, 0

    # 상어 좌표를 먹은 물고기 좌표로 이동
    shark_x, shark_y = nx, ny

    # 먹은 물고기 개수랑 상어 사이즈 업데이트
    count += 1
    if count == shark_size:
        shark_size += 1
        count = 0


print(time)