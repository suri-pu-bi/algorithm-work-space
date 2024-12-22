import sys
N, K = map(int, sys.stdin.readline().split())

round_desk = [i+1 for i in range(N)]
result = []
current = 0
while round_desk:
    current += K - 1 # K-1번째 인덱스까지 건너뛰기
    if current >= len(round_desk): # 인덱스가 범위를 넘어갈 경우
        current %= len(round_desk) # 나머지 연산을 통해 인덱스 계산

    result.append(str(round_desk.pop(current)))


print("<", ", ".join(result), ">", sep="")