import sys
def cut(x,y,n):
    # 처음 시작점을 정해두고, for문을 돌면서 그 시작점과 다른 값을 가지는 게 있으면 n//2로 분할
    # 왜? -> 현재 종이가 모두 같은 색으로 칠해져 있지않으면 현재 종이 기준 4등분으로 나누기 때문
    global white, blue
    color = paper[x][y]

    # 분할
    for i in range(x, x+n): # 세로
        for j in range(y, y+n): # 가로
            if paper[i][j] != color:
                cut(x, y, n // 2) # 1사분면
                cut(x,y + n//2, n//2) # 2사분면
                cut(x + n//2, y , n//2) # 3사분면
                cut(x + n//2 , y + n//2, n//2) # 4사분면
                return # 함수 종료조건, 그 뒤 반복문 실행되면 X

    # for문이 끝나면 가장 작은 단위까지 간 것 (모두 color(시작점)의 색깔)
    # color(시작점)이 1인지 0인지 확인하면 됨
    if color == 1:
        blue += 1

    else:
        white += 1


n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white = 0
blue = 0

cut(0,0,n)
print(white, blue, sep='\n')