import sys

read = sys.stdin.readline


def dfs(len, idx):
    if len == l:
        vo = 0
    else:
        for i in range(idx, c):
            if not check[i]:
                result.append(arr[i])


l, c = map(int, read().split())
check = [False for i in range(c)]
result = []
arr = read().split()
arr.sort()
dfs(0, 0)
