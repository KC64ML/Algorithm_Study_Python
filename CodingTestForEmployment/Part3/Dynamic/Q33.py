n = int(input())

list_array = [[0]]
dp = [0] * 16


for idx in range(1, n + 1):
    list_array.append(list(map(int, input().split())))
    dp[idx] = idx + list_array[idx][0]



total_result = 0
for i in range(1, n+1):

print(total_result)
