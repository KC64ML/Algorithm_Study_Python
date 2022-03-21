from sys import stdin as s
from collections import deque


def bfs(start, group, graph):
    cur_direction = 1
    queue = deque()
    queue.append((start, cur_direction))
    group[start] = 1

    while queue:
        node, cur_direction = queue.popleft()
        # print("현재 데이터 : ", node, "현재 그룹 : ", cur_direction)
        for cur_node in graph[node]:
            # 만약 group의 cur_node 인덱스 값이 0이라면 방문하도록
            if group[cur_node] == 0:
                group[cur_node] = -cur_direction
                # print("방문하게 됨, cur_node : ", cur_node, " cur_direction : ", -cur_direction)
                queue.append((cur_node, -cur_direction))
            elif group[cur_node] == cur_direction:
                # 이미 방문을 한 정점이 같은 그룹에 있는지 확인
                # print("이미 방문한 지를 확인한다. cur_node : ", cur_node, " cur_direction : ", cur_direction, "group[", cur_node,
                #       "] : ", group[cur_node])

                return False
                # 만약 현재 노드의 그룹 값과 같은 공간에 (방향이 같다면) False

    return True


k = int(s.readline())

for _ in range(k):
    v, e = map(int, s.readline().split())
    group = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]
    result = "YES"

    for idx in range(e):
        a, b = map(int, s.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for idx in range(1, v + 1):
        if group[idx] == 0:
            if not bfs(idx, group, graph):
                result = "NO"
                break

    print(result)
