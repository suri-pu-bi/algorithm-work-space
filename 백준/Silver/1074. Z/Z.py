import sys

# 분할 탐색을 시행할 때 중요한 점: 모든 부분을 분할하여 탐색하면 x
# 전체부터 시작하여 작은 부분으로 내려감

def solve(x, y, size):

    global result

    if x == r and y == c:
        print(result)
        sys.exit(0) # 프로그램 종료

    if size == 1:  # size가 1이면 더이상 분할X
        result += 1
        return  # 함수 종료

    # 시작 지점에서 한 변의 길이를 더한 범위 내에 r과 c가 포함된다면 분할탐색하기
    # 포함하지 않는다면 변의 제곱을 반환하여 칸 수를 한번에 계산해서 result return
    # -> z 순서대로 숫자 이어나가야 하기 때문

    if not (x <= r < x + size and y <= c < c + size): # 인덱스 범위 잘 보기
        result += size * size
        return # 함수 종료

    # 분할 # z순서대로
    solve(x, y, size//2) # 1
    solve(x, y + size//2, size//2) # 2
    solve(x + size//2 , y, size//2) # 3
    solve(x + size//2, y + size//2, size//2) # 4



n, r, c = map(int, sys.stdin.readline().split())
result = 0
solve(0,0,2**n)

