import sys

sys.setrecursionlimit(2 ** 8)

read = sys.stdin.readline

n = int(read())

graph = []

for _ in range(n):
    graph.append(list(map(int, read().split())))

graph.sort()

result = 0


def dfs(time, i, cnt):
    # print("인덱스 : ", i, "시작지점 : ", time, "시간 : ", cnt)
    global result

    if result < cnt:
        result = cnt

    for idx in range(i, n):
        if graph[idx][0] >= time and not visited[idx]:
            visited[idx] = True
            dfs(graph[idx][1], idx, cnt + 1)
            visited[idx] = False


for i in range(n):
    visited = [False] * (n + 1)

    visited[i] = True

    dfs(graph[i][1], i, 1)

    # print("현재 인덱스 : ", i, "결과 : ", result)
    # print()
print(result)
