from copy import deepcopy


# 왼쪽으로 기울이는 경우 먼저 생각
# 각 방향에 대해 따로 구현할 수도 있음
# -> 근데 생각해보면 board 자체를 회전하면 날로 먹을 수 있다!


def rotate(board, dir):
    turn90 = list(map(list, zip(*board[::-1])))
    turn180 = list(map(list, zip(*turn90[::-1])))
    turn270 = list(map(list, zip(*turn180[::-1])))

    if dir == 0:
        return board

    elif dir == 1:
        return turn90

    elif dir == 2:
        return turn180

    else:
        return turn270


def tilt (board, dir):
    rotate_board = rotate(board, dir)
    for i in range(n):
        new_arr = [0 for _ in range(n)]
        idx = 0
        for j in range(n):
            # 주어진 배열에 원소가 없으면 뒤에 내용을 실행하지 않는다.
            if rotate_board[i][j] == 0:
                continue
            # 새로운 배열 idx에 원소가 없으면, 해당하는 배열 값을 넣는다.
            if new_arr[idx] == 0:
                new_arr[idx] = rotate_board[i][j]
            # 새로운 배열 idx에 원소가 있는데, 해당하는 배열값과 같으면 두배를 곱한다.
            elif new_arr[idx] == rotate_board[i][j]:
                new_arr[idx] *= 2
                idx += 1
            # 새로운 배열 idx에 원소가 있는데, 해당하는 배열값과 다르면, 그 다음 idx에 해당하는 배열값을 넣는다.
            else:
                idx += 1
                new_arr[idx] = rotate_board[i][j]

        for j in range(n):
            rotate_board[i][j] = new_arr[j]


    return rotate_board


def select_dir(board, cnt):
    # 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 구하기 위한 변수
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, board[i][j])
        return

    for i in range(4):
        tmp_board = tilt(deepcopy(board), i)
        select_dir(tmp_board, cnt + 1)


import sys
n = int(sys.stdin.readline())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

ans = 0
select_dir(board, 0)
print(ans)