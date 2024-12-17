import sys
N = int(sys.stdin.readline())
graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 플로이드 와샬 알고리즘 : 거쳐가는 정점을 기준으로 최단거리르 구함
for k in range(N):
    for i in range(N):
        for j in range(N):
            # 0, 1 / 1, 3 이어져있으면 0, 3도 이어져있는 것
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for row in graph:
    print(' '.join(map(str, row)))