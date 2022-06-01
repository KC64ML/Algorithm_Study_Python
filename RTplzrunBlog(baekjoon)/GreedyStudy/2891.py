import sys

read = sys.stdin.readline

n, s, r = map(int, read().split())

arr = [0] * (n)

arr = [-200] + arr

damage = list(map(int, read().split()))
heal = list(map(int, read().split()))

for in_d in damage:
    arr[in_d] += -1
for in_h in heal:
    arr[in_h] += 1


def binary_divide(start, end):
    if start > end:
        return

    mid = (start + end) // 2

    if arr[mid] == 1:
        if mid - 2 > 0 and arr[mid - 1] == -1 and arr[mid - 2] == -1:
            arr[mid - 1], arr[mid] = 0, 0
        elif mid + 2 <= n and arr[mid + 1] == -1 and arr[mid + 2] == -1:
            arr[mid + 1], arr[mid] = 0, 0
        elif mid - 1 > 0 and arr[mid - 1] == -1:
            arr[mid - 1], arr[mid] = 0, 0
        elif mid + 1 <= n and arr[mid + 1] == -1:
            arr[mid], arr[mid + 1] = 0, 0

    binary_divide(start, mid - 1)
    binary_divide(mid + 1, end)


binary_divide(1, n)

print(arr.count(-1))
