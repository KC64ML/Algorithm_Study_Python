n = int(input())

dp = [0] * (n + 1)

arr = [0]

for _ in range(n):
    arr.append(int(input()))

dp[1] = arr[1]

for idx in range(2, n + 1):
    if idx == 2:
        dp[idx] = arr[1] + arr[2]
    else:
        dp[idx] = max(dp[idx - 2] + arr[idx], dp[idx - 1] + arr[idx], dp[idx - 2] + dp[idx - 1])

print(dp)

# https://pacific-ocean.tistory.com/152 참고하기


