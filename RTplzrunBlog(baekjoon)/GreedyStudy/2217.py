import sys

read = sys.stdin.readline

n = int(read())

arr = []

for i in range(n):
    arr.append(int(read()))

arr.sort(reverse=True)
answer = 0
for i in range(len(arr)):
    arr[i] *= (i + 1)

print(max(arr))
