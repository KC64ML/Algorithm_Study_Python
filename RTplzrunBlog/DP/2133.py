n = int(input())

dp = [0] * (n + 1)

if n >= 2:
    dp[2] = 3


    # (1) 길이 n일 때는 가운데 넣은 방법 2개가 있다.
    # (2) 이외 길이 n - 4까지는 아래, 위로 방향만 바꾸면 된다. (2가지)
    # (3) n - 2에서는 길이 2가 추가된다. (길이 2는 경우의 총 3가지)
    for i in range(4, n + 1, 2):
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2

print(dp[n])

# 참고 : https://suri78.tistory.com/103
