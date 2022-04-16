# import sys
# from itertools import combinations
#
# read = sys.stdin.readline
#
# n, s = map(int, read().split())
#
# arr = list(map(int, read().split()))
#
# result = 0
#
# for i in range(1, n+1):
#     check_data = combinations(arr, i)
#
#     for c in check_data:
#         if sum(c) == s:
#             result += 1
#
# print(result)

import sys

read = sys.stdin.readline

n, s = map(int, read().split())

arr = list(map(int, read().split()))

result = []

cnt = 0


def dfs(idx):
    global cnt
    if len(result) > 0 and sum(result) == s:
        cnt += 1

    for i in range(idx, n):
        result.append(arr[i])
        dfs(i + 1)
        result.pop()


dfs(0)

print(cnt)
