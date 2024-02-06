import sys

# 똑같은 코드가 적힘 -> 바깥으로 빼내서 생각 -> 상하좌우 좌표 활용
def move(mode):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if mode == 1:
        dice[0], dice[1], dice[2], dice[5] = f, a, b, c

    elif mode == 2:
        dice[0], dice[1], dice[2], dice[5] = b, c, f, a

    elif mode == 3:
        dice[1], dice[3], dice[4], dice[5] = e, b, f, d

    else:
        dice[1], dice[3], dice[4], dice[5] = d, f, b, e


input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
board = [] # map 변수 -> 파이썬 에러뜸

for _ in range(n):
    board.append(list(map(int, input().split())))

orders = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]

#    d
# a, b, c
#    e
#    f


# 동 : 1, 서 : 2, 북 : 3, 남 : 4
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

nx, ny = x, y
for i in orders:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue

    move(i)

    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1] # dice[5]가 항상 아래쪽면

    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[1]) # dice[1]이 항상 위쪽면

