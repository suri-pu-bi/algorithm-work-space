for _ in range(int(input())):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(2)]

    dp[0][0], dp[1][0] = sticker[0][0], sticker[1][0]

    # 기저상태
    if n >= 2:
        dp[0][1], dp[1][1] = dp[1][0] + sticker[0][1], dp[0][0] + sticker[1][1]


    for i in range(2, n):
        # 윗줄과 아래줄 위치가 대각선 위치이므로 둘 중 max값을 구해서 현재 값과 더해준다
        dp[0][i] = sticker[0][i] + max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] = sticker[1][i] + max(dp[0][i - 1], dp[0][i - 2])

    print(max(dp[0][n-1], dp[1][n-1]))