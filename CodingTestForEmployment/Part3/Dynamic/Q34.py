n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
# array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0,  i):
        # print("array[j] : ", array[j] , " array[i] : ",array[i])
        if array[j] < array[i]:
            print()
            print("i, j " , i, j ,", array[j] : ", array[j], " array[i]", array[i] , ", dp[i] : ", dp[i], ", dp[j] + 1 :", dp[j] + 1)
            dp[i] = max(dp[i], dp[j] + 1)



print(dp)
# 열외시켜야 하는 병사의 최소 수를 출력
print(n - max(dp))
