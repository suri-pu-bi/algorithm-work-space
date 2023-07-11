import sys
t = int(sys.stdin.readline())


for _ in range(t):
    n = int(sys.stdin.readline())
    cnt = 1

    scores = [0] * (n + 1) # 왼쪽 성적은 어쩌파 정렬 -> 인덱스처럼 받을 리스트 설정
    for _ in range(n):
        a,b = map(int,sys.stdin.readline().split())
        scores[a] = [b]

    minValue = scores[1] # 첫번째 점수의 1등
    
    for i in range(2,n+1):
        if scores[i] < minValue:
            minValue = scores[i]
            cnt += 1

    print(cnt)