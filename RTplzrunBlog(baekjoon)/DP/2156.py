n = int(input())

dp = [0] * (n + 1)

arr = [0]

for _ in range(n):
    arr.append(int(input()))

# ① 현재 포도주와 이전 포도주를 마시고 전전 포두주는 마시지 않는다. ( wine[i]+wine[i-1]+d[i-3] )
# ② 현재 포도주와 전전 포도주를 마시고 이전 포도주는 마시지 않는다. ( wine[i]+d[i-2] )
# ③ 현재 포도주를 마시지 않는다. ( d[i-1] )

# d[i-1]에 해당 케이스를 포함한 최댓값이 저장되어 있다.


dp[1] = arr[1]

if n >= 2:
    dp[2] = arr[1] + arr[2]

    for idx in range(3, n + 1):
        dp[idx] = max(dp[idx-1], dp[idx - 2] + arr[idx], dp[idx - 3] + arr[idx - 1] + arr[idx])

print(dp[n])

# 참고 : https://hongcoding.tistory.com/48


