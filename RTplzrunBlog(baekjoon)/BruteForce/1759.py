import sys

read = sys.stdin.readline


def dfs(len, idx):
    if len == l:
        vo = 0
        co = 0
        for i in range(l):
            if result[i] in 'aeiou':
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print(''.join(result))
        return
    else:
        for i in range(idx, c):
            if not check[i]:
                result.append(arr[i])
                check[i] = True
                dfs(len + 1, i + 1)
                check[i] = False
                del result[-1]  # 배열 마지막 공간 제거


l, c = map(int, read().split())
check = [False] * c
result = []
arr = read().split()
arr.sort()
dfs(0, 0)
