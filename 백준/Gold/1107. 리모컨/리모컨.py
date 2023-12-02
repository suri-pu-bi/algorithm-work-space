import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
ans = abs(100 - n) # ++, --로 이동할 경우 -> 최솟값으로 설정
if m: # 고장난게 있을 경우에만 input을 받음
    broken = set(sys.stdin.readline().split())
else:
    broken = set()

# 작은 수 -> 큰 수 이동 : 500,000까지 보면 됨
# 반대로 큰수 -> 작은 수 이동 : 1,000,000까지 봐야함

# for-else문: for문이 break 등으로 중간에 빠져나오지않고 끝까지 실행된 경우 else문 실행
for i in range(1000001):
    for num in str(i): # 1~1,000,000까지 모든 숫자의 자릿수마다 탐색
        if num in broken: # 그 해당하는 숫자버튼이 고장난 경우
            break # 다음 숫자로 이동
    else: # for문을 다 돌았는데 해당하는 숫자버튼이 고장난 것이 없을 때
        # 최솟값 갱신
        ans = min(ans, len(str(i)) + abs(i-n)) # 기존답, 숫자버튼 클릭수 + '+/-' 버튼 클릭 수

print(ans)