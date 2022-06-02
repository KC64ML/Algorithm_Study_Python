import sys

read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))

arr.sort()

answer = float(sys.maxsize)

for i in range(n * 2 // 2):
    cur_data = arr[i] + arr[2*n - i - 1]
    if answer > cur_data:
        answer = cur_data

print(answer)
