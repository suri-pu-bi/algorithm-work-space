for test_case in range(1, 11):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    max_value = 0
    
    # 가로 최댓값 계산
    for i in range(100):
        row_sum = sum(arr[i])
        if max_value < row_sum:
            max_value = row_sum
    
    # 세로 최댓값 계산
    for i in range(100):
        col_sum = 0
        for j in range(100):
            col_sum += arr[j][i]  
        
        if max_value < col_sum :
            max_value = col_sum
    
    # 대각선 최댓값 계산
    left_cross_value = 0
    right_cross_value = 0
    
    for i in range(100): # i=j & i+j=99
        left_cross_value += arr[i][i]
        right_cross_value += arr[i][99-i]
            
    max_value = max(max_value, left_cross_value, right_cross_value)
    print(f'#{num} {max_value}')
            
              
