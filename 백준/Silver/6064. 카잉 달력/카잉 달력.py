import sys
import math
'''
x의 주기 : M ex) M=10, N=12이고 x=3인 경우는 3, 13, 23, 33, 43, 53번째 해일 때
y의 주기 : N ex) M=10, N=12이고, y=5인 경우는 5, 17, 29, 41, 53번째 해일 때 

53번째 해를 M, N으로 나눈 나머지를 구하면, <x,y>로 표현 가능 ex) <53 % 10 = 3, 53 % 12 = 5>
종말하는 마지막 해 : <M, N>이 나타날 수 있는 최소 지점은 두 주기 M과 N의 최소공배수 
'''


def check(M, N, x, y):
    # 최소공배수 = 전체 배수 // 최대공약수
    lcm = M * N // math.gcd(M, N)

    # 최소공배수 내에서 탐색해 탐색효율 높임
    # x에서 시작해 y와 일치하는지 확인 ex) x = 3, 13, 23, 33 ..
    while x <= lcm:
        # ex) x가 33번째 해일때, 33 % 12 = 9가 y와 같은지 확인
        # 나머지가 0이 나오는 경우가 있는데, 달력은 1부터 시작하므로 (x-1) % N + 1로 표현
        if (x - 1) % N + 1 == y:
            return x
        x += M # x를 M 주기로 증가

    return -1


T = int(sys.stdin.readline())
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    print(check(M, N, x, y))