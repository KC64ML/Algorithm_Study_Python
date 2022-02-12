from sys import stdin as s

a, b = map(int, s.readline().split())
m = int(s.readline())

arr = list(map(int, s.readline().split()))

arr = [0] + arr

a_result = arr[m]

if m > 1:
    for idx in range(1, m):
        a_result += pow(a, m - idx) * arr[idx]


print(a_result)

