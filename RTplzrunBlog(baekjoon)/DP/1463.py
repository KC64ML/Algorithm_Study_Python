n = int(input())

dp = [0] * (n + 1) # dp에 초기값 0을 저장한다.

# bottom-Up 방식
# 2부터 n까지 dp 값을 구한다.
# 먼저 1을 더해준다. (이유는 먼저 더해도 어차피, 그 값이 2와 3으로 나누어지면 나누어진 값 중 최소 값으로 변경 가능하기 때문)
# 2에 n + 1까지
for cur_num in range(2, n + 1):
    # 먼저 1을 더해준다.
    dp[cur_num] = dp[cur_num - 1] + 1

    # 3으로 나누어 떨어지는지 본다.
    if cur_num % 3 == 0:
        # 현재 값이 3의 배수라면 확인한다.
        dp[cur_num] = min(dp[cur_num], dp[cur_num // 3] + 1)

    # 2로 나누어 떨어지는지 본다.
    if cur_num % 2 == 0:
        # 현재 값이 2의 배수라면 확인한다.
        dp[cur_num] = min(dp[cur_num], dp[cur_num // 2] + 1)

print(dp[n])