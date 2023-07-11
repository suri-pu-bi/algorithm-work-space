# 어디에 벽을 세워야 최댓값이 나올지 알 수 없다 -> 벽을 세울 수 있는 모든 경우의 수를 탐색해야함
# 백트래킹, BFS 이용
import copy
from collections import deque
import sys


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(): # 바이러스 퍼트리기
    # 바이러스를 퍼트리면 2로 다 바꾸게 되므로 테스트할 맵 따로 만들기
    test_graph = copy.deepcopy(graph)

    queue = deque()
    # 큐에다가 2의 위치 (바이러스의 위치) 다 넣기
    for i in range(n):
        for j in range(m):
            if test_graph[i][j] == 2:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            x_pos, y_pos = x + dx[i], y + dy[i]
            if 0<=x_pos<n and 0<=y_pos<m:
                if test_graph[x_pos][y_pos] == 0:
                    test_graph[x_pos][y_pos] = 2
                    queue.append((x_pos,y_pos))

    # ---- 바이러스 다 퍼짐
    global result
    cnt = 0
    for i in range(n):
        for j in range(m):
            if test_graph[i][j] == 0:
                cnt += 1

    result = max(result, cnt) # result 갱신

def make_wall(count): # 벽 세우기
    if count == 3: # 벽의 개수가 3이면 bfs 돌려서 바이러스 퍼트리기
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: # 0인 것이 있으면
                graph[i][j] = 1 # 벽 세우기
                make_wall(count + 1) # 재귀
                graph[i][j] = 0 # return으로 종료되면 다시 원래대로 돌리기


n,m = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

result = 0
make_wall(0)

print(result)
