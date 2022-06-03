# 문자열에서 가장 긴 문자열을 찾아
# 0번째 문자열 값이 가장 큰 값이다.

# dist['A'] += (현재 i번째 행의 문자열 길이 - 인덱스)

import sys

read = sys.stdin.readline

n = int(read())
arr = []

for i in range(n):
    arr.append(list(read().rstrip()))

dist = {}

for i in range(ord('J') - ord('A') + 1):
    dist[chr(ord('A') + i)] = 0

for in_arr in arr:
    for i in range(len(in_arr)):
        dist[in_arr[i]] += len(in_arr) - i

l_dist = list(dist.items())
l_dist.sort(key= lambda x:-x[1])

dist = dict(l_dist)
# 딕셔너리를 9 ~ 1로 하고, 숫자로 변경한다.