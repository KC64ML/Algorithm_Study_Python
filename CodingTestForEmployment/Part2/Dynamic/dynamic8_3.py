# 정수 N을 입력받기
n = int(input())

# 모든 식량 정보 입력받기
list_array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [0] * 1001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for idx in range(0, n):
    if idx == 0 or idx == 1:
        dp[idx] = list_array[idx]
    else:
        dp[idx] = max(dp[idx - 1], dp[idx - 2] + list_array[idx])

# 계산된 결과 출력
print(dp[n - 1])