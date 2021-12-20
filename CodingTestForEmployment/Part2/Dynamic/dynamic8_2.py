x = int(input())

dp = [0] * 30001
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 1


for idx in range(6, 31):
    two_data = 9999999
    three_data = 9999999
    five_data = 9999999


    if idx % 5 != 0 and idx % 3 != 0 and idx % 2 != 0:
        idx -= 1

    if idx % 5 == 0:
        five_data = dp[idx // 5] + 1
    elif idx % 3 == 0:
        three_data = dp[idx // 3] + 1
    elif idx % 2 == 0:
        two_data = dp[idx // 2] + 1

    result = min(five_data, three_data, two_data)
    dp[idx] = result


print(dp[x])
