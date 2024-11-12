T = int(input())
password = [ '0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    
    graph = [input() for _ in range(n)]
    code = ''
    cnt = 0
    flag = False
    for i in range(n):
        if flag == True:
            break
        # find는 문자열일 때만, 리스트면 in 사용하기
        index = graph[i].rfind('1') # 문자열이므로 '' 붙이기
        if  index != -1:
            for j in range(index, -1, -1): # 맨 마지막 index 조심, 암호 모두 1로 끝나기 때문에 뒤에서부터 파싱
                if cnt == 56:
                    flag = True
                    break
                code += graph[i][j]
                cnt += 1
        
    code = code[::-1] # 문자열 뒤집기, 리스트는 reverse()
    code_result = []
    for i in range(0, 57, 7):
    	for j in range(10):
            if password[j] == code[i:i+7]:
                code_result.append(j)
   
    even_sum = 0
    odd_sum = 0
    for i in range(8):
        if i % 2 == 0:
            odd_sum  += code_result[i]
        else:
            even_sum += code_result[i]
    
    result = even_sum + odd_sum * 3
    
    if result % 10 == 0:
        print(f'#{test_case} {sum(code_result)}')
    else:
        print(f'#{test_case} 0')
