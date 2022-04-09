import sys

sys.setrecursionlimit(50000000)

read = sys.stdin.readline

n, s = map(int, read().split())

arr = list(map(int, read().split()))

result = 999999


def dfs(cur_idx, cur_sum, cur_cnt):
    global result

    if cur_sum >= s:
        result = min(result, cur_cnt)

    if cur_idx == n:
        return

    dfs(cur_idx + 1, cur_sum, cur_cnt)
    dfs(cur_idx + 1, cur_sum + arr[cur_idx], cur_cnt + 1)


dfs(0, 0, 0)

print(result if result != 999999 else 0)


# dfs로는 안된다.