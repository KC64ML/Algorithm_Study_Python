# n = int(input())
#
# dp = []
#
# for idx in range(n + 1):
#     dp.append(idx)
#
# for i in range(2, n+ 1):
#     for j in range(2, i+1):
#         if j * j > i:
#             break
#         else:
#             dp[i] = min(dp[i], dp[i - j * j] + 1)
#
# print(dp[n])


# 참고하여 수정한 코드

n = int(input())

dp = [0] * (n + 1)

for i in range(1, n+ 1):
    dp[i] = i
    j = 1

    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

print(dp[n])
