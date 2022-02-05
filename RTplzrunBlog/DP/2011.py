# rstrip : 공백 제거

pw = list(map(int, input().rstrip()))

dp = [0] * (len(pw) + 1)

dp[0] = 1

if len(pw) >= 1:

    pw = [0] + pw
    dp[1] = 1

    for idx in range(2, len(pw)):
        print(idx)
        if 10 <= pw[idx - 1] * 10 + pw[idx] <= 26:
            # 현재 위치에서 2번째 뒤로
            dp[idx] += dp[idx - 2]
            print("10 과 26 사이, ", idx,  dp[idx])

        if 1 <= pw[idx] <= 9:
            dp[idx] += dp[idx - 1]

print(dp[len(pw) - 1])