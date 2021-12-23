n = int(input())

list_array = []
dp = [[0] * n for _ in range(n)]

for idx in range(n):
    list_array.append(list(map(int, input().split())))


col_idx = 0
dp[0][0] = list_array[0][0]


for row in range(1, n):
    for col in range(0, len(list_array[row])):
        if col == 0:
            dp[row][col] = dp[row-1][col] + list_array[row][col]
        elif col == len(list_array[row]) - 1:
            dp[row][col] = dp[row -1][col - 1] + list_array[row][col]
        else:
            dp[row][col] = max(dp[row - 1][col - 1], dp[row - 1][col]) + list_array[row][col]


print(max(dp[n-1][0:n]))


