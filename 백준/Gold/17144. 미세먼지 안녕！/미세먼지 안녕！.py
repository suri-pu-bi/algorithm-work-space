# 확산
def spread(dust):
    for i in range(len(dust)):
        amount = dust[i][2] // 5
        cnt = 0
        for j in range(4):
            nx = dust[i][0] + dx[j]
            ny = dust[i][1] + dy[j]

            if nx < 0 or nx >= r or ny < 0 or ny >= c or room[nx][ny] == -1:
                continue

            room[nx][ny] += amount
            cnt += 1

        room[dust[i][0]][dust[i][1]] -= amount * cnt


# 공기청정기 작동 : 뒤에서부터?
def work(x, mode):

    if mode == 0:

        for i in range(x-1, 0, -1):
            tmp = room[i-1][0]
            room[i][0] = tmp

        for i in range(c-1):
            tmp = room[0][i+1]
            room[0][i] = tmp

        for i in range(x):
            tmp = room[i+1][c-1]
            room[i][c-1] = tmp

        for i in range(c-1, 0, -1):
            if room[x][i-1] == -1:
                room[x][i] = 0
                break
            tmp = room[x][i-1]
            room[x][i] = tmp

    else:

        for i in range(x+1, r-1):
            tmp = room[i+1][0]
            room[i][0] = tmp

        for i in range(c-1):
            tmp = room[r-1][i+1]
            room[r-1][i] = tmp

        for i in range(r-1, x, -1):
            tmp = room[i-1][c-1]
            room[i][c-1] = tmp

        for i in range(c-1, 0, -1):
            if room[x][i-1] == -1:
                room[x][i] = 0
                break
            tmp = room[x][i - 1]
            room[x][i] = tmp


import sys
input = sys.stdin.readline
r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]



for i in range(t):
    dust = []
    for j in range(r):
        for k in range(c):
            if room[j][k] != 0 and room[j][k] != -1:
                dust.append((j, k, room[j][k]))

    spread(dust)

    index = 0
    for j in range(r):
        if room[j][0] == -1:
            work(j, index)
            index += 1

answer = 0
for i in range(r):
    answer += sum(room[i])


print(answer+2)
