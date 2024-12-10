import sys
N, M = map(int, sys.stdin.readline().split())
dict = {}

for _ in range(N):
    site, password = sys.stdin.readline().rstrip().split()
    dict[site] = password

for _ in range(M):
    site = sys.stdin.readline().rstrip()
    print(dict[site])