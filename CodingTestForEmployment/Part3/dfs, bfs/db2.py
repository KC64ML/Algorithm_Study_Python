n, m = map(int, input().split())
data = [] # 초기 list
temp = [[0] * m for _ in range(n)] # 결과가 저장된 list

for _ in range(n):
    data.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 바이러스 넣을 자리 dfs 수행
def virus(x, y):
    for idx  in range(4):
        next_x = x + dx[idx]
        next_y = y + dy[idx]
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
            continue
        if temp[next_x][next_y] == 0:
            temp[next_x][next_y] = 2
            virus(next_x, next_y)


def get_zero_cnt():
    zero_cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                zero_cnt += 1

    return zero_cnt

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    # 바이러스 위치라면 전파하기
                    virus(i,j)
        # 0의 개수 찾기
        result = max(result, get_zero_cnt())
        return result
    else:
        for i in range(n):
            for j in range(m):
                if data[i][j] == 0:
                    data[i][j] = 1
                    count += 1
                    dfs(count)
                    data[i][j] = 0
                    count -= 1



dfs(0)
print(result)