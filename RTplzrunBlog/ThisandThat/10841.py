from sys import stdin as s

n = int(s.readline())

arr = []

for _ in range(n):
    arr.append(list(s.readline().split()))

arr.sort(key=lambda x: int(x[0]))

for num, data in arr:
    print(num, data)
