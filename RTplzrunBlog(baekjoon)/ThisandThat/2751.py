import sys

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))


for data in sorted(arr):
    print(data)


# https://leunco.tistory.com/m/71


