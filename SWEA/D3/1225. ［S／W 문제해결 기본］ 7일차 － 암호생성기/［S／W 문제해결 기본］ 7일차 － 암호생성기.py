from collections import deque 

def generate_code(code):
    while True:
        for i in range(1, 6):
            # 첫 번째 값을 꺼내고, 그 값에서 i를 뺀 값을 새로운 값으로 설정
            new_code = code[0] - i
            code.popleft()  # 첫 번째 값 제거
            
            # 만약 새로운 코드가 0 이하라면 0을 넣고 종료
            if new_code <= 0:
                code.append(0)
                return code
            
            code.append(new_code)  # 새로운 값 추가

for test_case in range(1, 11):
    num = int(input())
    code = deque(list(map(int, input().split())))
    generated_code = generate_code(code)
    
    print(f'#{num} {" ".join(map(str, generated_code))}')
    
                  
                  
        
