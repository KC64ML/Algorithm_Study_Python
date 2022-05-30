import sys

read = sys.stdin.readline

n = int(read())
k = int(read())

sensor = list(map(int, read().split()))

sensor.sort()

minusSection = []
answer = 0

for i in range(n-1):
    minusSection.append(abs(sensor[i] - sensor[i+1]))


minusSection.sort(reverse=True)
for i in range(k-1, n-1):
    answer += minusSection[i]

print(answer)