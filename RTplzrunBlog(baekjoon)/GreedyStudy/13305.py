import sys

read = sys.stdin.readline

n = int(read())

length = list(map(int, read().split()))
price = list(map(int, read().split()))

length = length + [0]
city = []

for x, y in zip(length, price):
    city.append([x, y])

del city[len(city) - 1]

answer = city[0][0] * city[0][1]
minidx = 0

for i in range(1, len(city)):
    if city[minidx][1] * city[i][0] > city[i][0] * city[i][1]:
        minidx = i
        answer += city[i][0] * city[i][1]
    else:
        answer += city[minidx][1] * city[i][0]

print(answer)
