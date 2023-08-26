import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
operation = list(map(int, sys.stdin.readline().split()))


# max값, min값 초기화
maximum = -1e9 # -10억
minimum = 1e9 # 10억

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == n: # depth = 현재 사용한 숫자의 개수
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)

    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)

    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)

    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)



# 순서대로 계산하므로 루트 노트가 num[0]
dfs(1, num[0], operation[0], operation[1], operation[2], operation[3])

print(maximum)
print(minimum)