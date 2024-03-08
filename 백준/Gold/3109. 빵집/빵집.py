import sys
r, c = map(int, sys.stdin.readline().split())

graph = []
for _ in range(r):
    graph.append(list(sys.stdin.readline().rstrip()))

dx = [-1, 0, 1]
dy = [1, 1, 1]

visited = [[-1 for _ in range(c)] for _ in range(r)]
cnt = 0

def dfs(x, y):
    # dfs는 종료조건을 먼저 생각하기
    if y == c-1:
        return True

    for i in range(3):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] != 'x' and visited[nx][ny] == -1:
                visited[nx][ny] = 1
                if dfs(nx, ny):
                    return True
    return False


for i in range(r):
    if dfs(i, 0):
        cnt += 1

print(cnt)