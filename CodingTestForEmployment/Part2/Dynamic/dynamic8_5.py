n, m = map(int, input().split())

list_array = []
dp = [0] * 10001

for idx in range(n):
    list_array.append(int(input()))
    dp[list_array[idx]] = 1


list_array.sort()

for idx in range(1, m + 1):
    cur_data = -1
    if dp[idx] == 1:
        continue

    for k in range(len(list_array)):

        if idx % list_array[k] == 0 and (cur_data > dp[list_array[k]] + 1 or cur_data == -1):
            cur_data = dp[list_array[k]] + 1

    dp[idx] = cur_data
    print(dp[idx])

print(dp)