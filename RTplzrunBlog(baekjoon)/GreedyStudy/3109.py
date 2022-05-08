import sys

read = sys.stdin.readline

r, c = map(int, read().split())

graph = []
answer = 0

for i in range(r):
    graph.append(list(map(str, read().strip())))


def check_fun(row, col):
    # 방문한 곳은 다시 방문하지 못하게 한다. (확인한 곳은)
    graph[row][col] = 'a'

    # 위 3가지 조건 중에 적어도 하나에 계속 해당하다,
    # 열이 y-1번째(마지막 열)에 도착했다면 True를 return 해야한다.
    if col == c - 1:
        return True

    # 만약 행이 0보다 크고 (1)와 같이 (행-1, 열+1)이 `.`일 때
    if row > 0 and graph[row - 1][col + 1] == '.':
        if check_fun(row - 1, col + 1):
            return True

    # (2)와 같이 (행, 열+1)이 `.`일 때
    if graph[row][col + 1] == '.':
        if check_fun(row, col + 1):
            return True

    # 만약 행+1이 R(총 행 길이)보다 작고 (3)와 같이 (행+1, 열+1)이 `.`일 때
    if row + 1 < r and graph[row + 1][col + 1] == '.':
        if check_fun(row + 1, col + 1):
            return True

    # 위 3가지 조건에 해당하지 않는다면 최종적으로 False를 return 한다.
    return False


for i in range(r):
    if graph[i][0] not in 'X':
        if check_fun(i, 0):
            answer += 1

print(answer)
