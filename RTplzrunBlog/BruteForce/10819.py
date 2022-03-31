import sys

read = sys.stdin.readline

n = int(read())

arr = list(map(int, read().split()))
arr.sort()
result = [0] * len(arr)

mid = len(arr) // 2  # 중간 값

result[mid] = max(arr)
total = len(arr)
arr = [0] + arr
cnt = 1
idx = 1

while cnt <= total - 4:
    result[mid - idx] = arr[idx]
    result[mid + idx] = arr[idx + 1]
    result[mid - idx - 1] = arr[total - idx]
    result[mid + idx + 1] = arr[total - idx - 1]

    # print(arr[idx + mid], arr[idx + mid + 1])
    cnt += 4
    idx += 2

# print(cnt, result)

check = False

# 4보다 작다면
if cnt + 1 == total:
    result[0] = arr[idx]
else:
    if not (len(arr) - 1) % 2:
        result[0] = arr[idx + 1]
        result[1] = arr[idx]
        result[total - 1] = arr[total - idx]
    else:
        result[0] = arr[idx]
        result[total - 1] = arr[total - idx]

# print(result)

total_result = 0

for i in range(1, n, 2):
    total_result += abs(result[i-1] - result[i])
    if i + 1 < n:
        total_result += abs(result[i] - result[i+1])

print(total_result)