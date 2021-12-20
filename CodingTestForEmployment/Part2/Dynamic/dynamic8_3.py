n = int(input())
list_array = list(map(int, input().split()))

dp = [0] * 1001

for idx in range(0, n):
    if idx == 0 or idx == 1:
        dp[idx] = list_array[idx]
    else:
        dp[idx] = max(dp[idx - 1], dp[idx - 2] + list_array[idx])

print(dp[n - 1])