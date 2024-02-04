import sys
from copy import deepcopy

# 백트래킹 문제라는 것은 파악했지만, DFS를 파악하지못했고, cctv 방향을 선택하고 어떻게 돌아와야하는지 파악하지못함

input = sys.stdin.readline
n, m = map(int, input().split())
cctv = []
office = []

# 튜플로 x좌표, y좌표로 구성 -> dic으로 바꿈, 굳이 x좌표/y좌표로 나눠서 넣지않음
# 각 cctv별로 감시할 수 있는 방향
direction = [
    [], # cctv가 없는 경우도 있을 수 있음
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

# 위 - 오 - 아래 - 왼
# direction 리스트가 이 좌표리스트의 인덱스를 나타내므로 cctv 방향 조건에 맞추어 북, 동, 남, 서 순서로 초기화
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


for i in range(n):
    data = list(map(int, input().split()))
    office.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            # cctv의 종류와 위치를 cctv 리스트를 업데이트
            cctv.append([data[j], i, j])


def fill(x, y, d, office_copy) :
    for i in d:
        nx = x
        ny = y
        while True:
            # 상하좌우 x좌표, y좌표 리스트 그대로 해놓고, cctv 방향을 좌표 리스트의 index로 설정해서 구함
            nx += dx[i]
            ny += dy[i]

            # 범위을 벗어났으면
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break

            # 벽을 만났다면
            if office_copy[nx][ny] == 6:
                break

            # 0이라면, '#'대신 '-1'로 변경시키기
            elif office_copy[nx][ny] == 0:
                office_copy[nx][ny] = -1


def dfs(depth, office):
    global answer

    if depth == len(cctv):
        count = 0

        # 사각지대 구하는 함수
        for i in range(n):
            count += office[i].count(0)

        # 각 케이스마다 사각지대 개수 가장 작은 값으로 업데이트
        answer = min(answer, count)
        return

    # 원래 office에 영향을 미치지 않게 하기 위해서 사용
    office_tmp = deepcopy(office)
    cctv_num, x, y = cctv[depth]

    for d in direction[cctv_num]:
        fill(x, y, d, office_tmp)
        dfs(depth + 1, office_tmp)
        # dfs 탐색 완료 후에 그 이전 상태로 돌리기 위해 사용 -> 그래야 dfs 탐색 중에 수행된 변경사항 취소가능
        office_tmp = deepcopy(office)


answer = int(1e9)
dfs(0, office)
print(answer)