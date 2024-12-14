import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

cur, cnt, answer = 0, 0, 0

while cur < M - 1:
    # 현재 반복되는 문자열이 'IOI'인지 확인
    if S[cur : cur+3] == 'IOI':
        # 다음에도 'IOI'가 반복되는지 확인
        cur += 2
        # 'IOI' 반복 수 저장
        cnt += 1
        # 반복 수 cnt가 N가 일치하는지 확인 = Pn을 찾은 것
        if cnt == N:
            answer += 1
            cnt -= 1 # 다음 반복 수까지 카운트했으므로 -1 해주기

    else:
        # 다음 인덱스로 이동, cnt 초기화
        cur += 1
        cnt = 0

print(answer)