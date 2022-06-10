import sys

read = sys.stdin.readline

n = int(read())
k = int(read())

sensor = list(map(int, read().split()))
s = []

sensor.sort()

for i in range(1, n):
    s.append(abs(sensor[i] - sensor[i-1]))

s.sort(reverse=True)
answer = 0

for i in range(k-1, n-1):
    answer += s[i]
print(answer)