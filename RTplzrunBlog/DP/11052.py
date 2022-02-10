import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * (n + 1)

arr = [0] + arr  # 0번째 인덱스 만들기

for i in range(1, n + 1):
    result = arr[i]

    cnt = 0
    if i % 2 == 0:
        cnt = i // 2
    else:
        cnt = (i // 2) + 1

    for j in range(1, cnt + 1):
        result = max(dp[i - j] + dp[j], result)
        # print("i, j", i, j, " 결과 : ", dp[n - j])

    dp[i] = result
    # print()


print(dp[n])
