#import sys
#sys.stdin = open("input.txt", "r")

'''
완전탐색(dfs) + 백트래킹
lst = [1, 2, 3]이고 N = 2일 때, 단계적으로 보면
1. 첫 번째 for 루프에서 (i, j) = (0, 1)을 선택하여 lst = [2, 1, 3]로 바꾸고, 재귀적으로 dfs 호출
2. dfs 호출이 끝나면 다시 lst = [1, 2, 3]로 복구하고, 다음 (i, j) = (0, 2)로 넘어가서 같은 과정을 반복
3. 각 단계에서 가능한 모든 교환을 시도하면서 최종적으로 가장 큰 수를 찾음
''' 
def dfs(n): # 함수 호출 전 정의 필요
    global answer
    if n == cnt :
        answer = max(answer, int("".join(num_list))) # 가장 큰 수 찾기
        return 
    
    for i in range(length - 1):
        for j in range(i+1, length): 
            num_list[i], num_list[j] = num_list[j], num_list[i] # 위치 바꾸기
            if (n, int("".join(num_list))) not in visited:
                dfs(n+1)
                visited.add((n, int("".join(num_list))))
            
            num_list[j], num_list[i] = num_list[i], num_list[j] # 백트래킹
            
T = int(input())

for test_case in range(1, T + 1):
    num, cnt = map(int, input().split())
    num_list = list(str(num))
    length = len(num_list)
    visited = set()
    answer = 0
    dfs(0)
    print(f'#{test_case} {answer}')
    
    
