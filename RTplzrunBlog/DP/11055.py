a = int(input())

dp = [0] * (a + 1)

arr = list(map(int, input().split()))

result = 0

for i in range(a):
    result = 0
    # print("idx : ", i)
    for j in range(i + 1):
        # print("현재 : ", i , j , " ",arr[i], dp[j])
        if arr[i] > arr[j]:
            result = max(dp[j], result)
            # print("i, j, result: ", i, j, result)

    # print("i", i ,"result : ", result, "arr[i]", arr[i])
    dp[i] = result + arr[i]




print(max(dp))
