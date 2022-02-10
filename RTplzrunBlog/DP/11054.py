n = int(input())

left_dp = [1] * (n + 1)
right_dp = [1] * (n + 1)

arr = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            left_dp[i] = max(left_dp[i], left_dp[j] + 1)

for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[j] < arr[i]:
            right_dp[i] = max(right_dp[i], right_dp[j] + 1)

result = 0

for i in range(n):
    result = max(result, left_dp[i] + right_dp[i] - 1)

print(result)
