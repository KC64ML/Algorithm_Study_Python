import sys
import heapq

read = sys.stdin.readline

t = int(read())

for i in range(t):
    k = int(read())
    filesizes = list(map(int, read().split()))
    twosumcost = []
    answer = 0
    for filesize in filesizes:
        heapq.heappush(twosumcost, filesize)

    while len(twosumcost) > 1:
        first = heapq.heappop(twosumcost)
        second = heapq.heappop(twosumcost)
        answer += (first + second)
        heapq.heappush(twosumcost, first + second)
    print(answer)
