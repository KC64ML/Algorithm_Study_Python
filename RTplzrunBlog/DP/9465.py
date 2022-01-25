t = int(input())

for _ in range(t):
    n = int(input())
    list_array = []
    dp = [[0] * (n) for _ in range(2)]

    for _ in range(2):
        list_array.append(list(map(int, input().split())))

    dp[0][0] = list_array[0][0]
    dp[1][0] = list_array[1][0]
    print(list_array[0])
    print(list_array[1])

    for i in range(2):

        if i == 1:
            cur_i = 0
        else:
            cur_i = 1

        for j in range(1, n):

            if j == 1:
                # print("i, j", i, j, "결과 : ", dp[cur_i][j - 1])
                dp[i][j] = dp[cur_i][j - 1] + list_array[i][j]
            else:
                print("i, j", i, j, "결과 : ", dp[cur_i][j - 2], dp[cur_i][j - 1])
                cur_data = max(dp[cur_i][j - 2], dp[cur_i][j - 1]) + list_array[i][j]
                if cur_data > dp[i][j]:
                    dp[i][j] = cur_data

    print(dp[0])
    print(dp[1])
