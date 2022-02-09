from sys import stdin as s

n = int(s.readline())

arr = [0] * 10010

# 데이터 개수가 많음 10,000,000

for _ in range(n):
    num = int(s.readline())
    arr[num] += 1

for idx in range(10001):
    for _ in range(arr[idx]):
        print(idx)




