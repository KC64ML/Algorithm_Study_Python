import sys

n = int(input())

arr = list(map(int, sys.stdin.readline().split()))

for idx in range(1, n):
    arr[idx] = max(arr[idx], arr[idx - 1] + arr[idx])

print(max(arr))