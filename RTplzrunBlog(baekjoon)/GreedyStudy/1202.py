import sys
import heapq

read = sys.stdin.readline

n, k = map(int, read().split())

listJewelry = []
listHeight = []

for _ in range(n):
    a, b = map(int, read().split())
    listJewelry.append([a, b])

for _ in range(k):
    a = int(read())
    listHeight.append(a)


listJewelry.sort()
listHeight.sort()

result = 0
temp = []

for i in listHeight:
    while listJewelry and i >= listJewelry[0][0]:
        heapq.heappush(temp, -listJewelry[0][1])

        heapq.heappop(listJewelry)

    if temp:
        result += heapq.heappop(temp)

print(-result)