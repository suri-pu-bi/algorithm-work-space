import sys
sys.setrecursionlimit(10000) # 재귀제한 문제 해결

def dfs(v):
    visited[v] = True # 방문처리
    for e in graph[v]: # 연결된 노드들 확인
        if not visited[e]: # 방문하지 않았다면
            dfs(e) # 끝까지 다 확인
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]  # 정점이 1번 부터 시작, index = 정점 번호
cnt = 0
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i) # dfs를 실행하면 visited에 연결된 노드들 모두 방문처리 되어있음
        cnt += 1 # 다음에 if문 조건을 만족시켜 방문하지 않은 노드가 나오면 새로운 연결요소!

print(cnt)