import sys

pw = list(map(int, sys.stdin.readline().rstrip()))

dp = [0] * (len(pw) + 1)

if pw[0] == 0:
    print("0")

else:
    pw = [0] + pw
    dp[0] = dp[1] = 1
    for idx in range(2, len(pw)):
        # 중간에 0이 있으면 이전 결과를 그대로 가져와야한다.
        if pw[idx] >= 1:
            dp[idx] += dp[idx - 1]
        print("현재")
        if 10 <= pw[idx - 1] * 10 + pw[idx] <= 26:
            dp[idx] += dp[idx - 2]
            print("idx 가", idx, "pw [", idx - 1, "] : ", pw[idx - 1], "pw [", idx, "] : ", pw[idx], "dp[idx - 1] : ",
                  dp[idx - 1], "dp[idx] : ", dp[idx])

    print(dp)
    print(dp[len(pw) - 1] % 1000000)

