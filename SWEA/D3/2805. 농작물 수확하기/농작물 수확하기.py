T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, list(input()))) for _ in range(n)]
    pivot = n // 2
    
    start, end = pivot, pivot
    result = 0
    flag = False
    for i in range(n):
        if start <= 0 and end >= n-1:
            flag = True
   		
        for j in range(start, end+1):
            result += graph[i][j]
  		
        if flag:
            start += 1
            end -= 1
        else:
            start -= 1
            end += 1
            
    print(f'#{test_case} {result}') 