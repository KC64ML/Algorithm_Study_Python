import sys

read = sys.stdin.readline

n = int(read())

graph = []

for _ in range(n):
    graph.append(list(map(int, read().split())))

graph.sort(key=lambda x: (x[1], x[0]))

endTime = graph[0][1]

result = 1

for idx in range(1, len(graph)):
    if graph[idx][0] >= endTime:
        endTime = graph[idx][1]
        result += 1

print(result)
