import sys

read = sys.stdin.readline

n = int(read())

city = []

for _ in range(n):
    city.append(list(map(int, read().split())))


def dfs(start, next, cost, cnt):
    global result

    # 만약 결과보다 큰 비용이라면 종료한다.
    if cost > result:
        return

    # 마지막 도시를 도착한 후
    if cnt == n:
        # 다시 시작점으로 돌아올 때, 0이 아닌 값이라면 (도시 거리가 0이 아니라면)
        if city[next][start]:
            result = min(result, cost + city[next][start])
        return

    for node_idx in range(n):
        if city[next][node_idx] and not visited[node_idx] and next != node_idx:
            visited[node_idx] = True

            # 시작점, 다음 노드, 현재까지 나온 비용 + 현재 도시와 다음 도시의 거리, 이때까지 만난 도시의 갯수
            dfs(start, node_idx, cost + city[next][node_idx], cnt + 1)
            visited[node_idx] = False


result = sys.maxsize
visited = [False] * (n + 1)

for i in range(n):

    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False

print(result)
