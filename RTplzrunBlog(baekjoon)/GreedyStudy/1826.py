import sys
import heapq

read = sys.stdin.readline

n = int(read())

gasStation = []

for _ in range(n):
    a, b = map(int, read().split())
    heapq.heappush(gasStation, [a, b])

l, p = map(int, read().split())

move = []
answer = 0

while p < l:

    # 주유소 정보가 있고, 주유소 위치가 연료양보다 작거나 같을 때
    while gasStation and gasStation[0][0] <= p:
        g, f = heapq.heappop(gasStation)
        # 우선순위 큐
        # 정렬을 할 때, 주유소에서 채울 수 있는 연료양으로 한다.
        # heap은 오름차순으로 정렬이 되므로
        # 연료양 * -1 을 하여, 내림차순으로 정렬을 한다.
        heapq.heappush(move, [-1 * f, g])

        # 최대힙이 비었다면 도달할 수 없는 의미로 -1을 출력한다.
    if not move:
        answer = -1
        break
    else:
        f, g = heapq.heappop(move)
        p += -1 * f
        # p는 연료 양을 의미한다.
        answer += 1

print(answer)