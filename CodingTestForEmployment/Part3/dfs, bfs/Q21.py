from collections import deque

n, l, r = map(int, input().split())

list_arr = []

for i in range(n):
    list_arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

total_cnt = 0



def bfs(x, y, visited):
    global cnt
    global list_sum
    list_find_bfs = []

    queue = deque()
    queue.append((x, y))
    while queue:
        cur_data = queue.popleft()

        for i in range(4):
            next_x = cur_data[0] + dx[i]
            next_y = cur_data[1] + dy[i]

            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
                continue
            if visited[next_x][next_y] == True:
                continue

            dis_data = abs(list_arr[cur_data[0]][cur_data[1]] - list_arr[next_x][next_y])
            if dis_data < l or dis_data > r:
                continue
            visited[next_x][next_y] = True

            cnt += 1
            list_find_bfs.append((next_x, next_y))
            list_sum += list_arr[next_x][next_y]
            queue.append((next_x, next_y))

    if len(list_find_bfs) != 0 and visited[x][y] == False:
        list_find_bfs.append((x, y))
        list_sum += list_arr[x][y]
    return list_find_bfs

while True:
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    list_sum = 0
    result = []

    for i in range(n):
        for j in range(n):
            if visited[i][j] == True:
                continue

            result += bfs(i, j, visited)


    for i in range(len(result)):
        for j in range(2):
            list_arr[result[i][0]][result[i][1]] = (list_sum // cnt)

    print(list_arr)

    if cnt == 0:
        break

    total_cnt += 1

print(total_cnt)