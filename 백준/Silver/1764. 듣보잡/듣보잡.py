import sys

N, M = map(int, sys.stdin.readline().split())
A = []
B = []
for _ in range(N):
    A.append(sys.stdin.readline().rstrip())

for _ in range(M):
    B.append(sys.stdin.readline().rstrip())

# set : 집합 데이터형 / 교집합
A = set(A)
B = set(B)

AB = list(A.intersection(B))
AB.sort()
print(len(AB))

for name in AB:
    print(name)