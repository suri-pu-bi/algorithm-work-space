# 테스트케이스가 10개라고 주어짐
for test_case in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0 
    for i in range(2, n - 2):
        # 주변 4개 건물과 비교하여 조망이 가능한지 확인
        if buildings[i] > buildings[i + 1] and buildings[i] > buildings[i + 2] and buildings[i] > buildings[i - 1] and buildings[i] > buildings[i - 2]:
            cnt += (buildings[i] - max(buildings[i - 1], buildings[i - 2], buildings[i + 1], buildings[i + 2]))
    
    print(f'#{test_case} {cnt}')