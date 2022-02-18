from sys import stdin as s
from collections import deque


def dfs(a, p):
    cur_data = 0
    for idx in range(len(a)):
        cur_data += pow(int(a[idx]), p)

    if visited[cur_data]:
        return cur_data

    visited[cur_data] = True
    queue.append(cur_data)
    return dfs(str(cur_data), p)


a, p = s.readline().split()
p = int(p)

visited = [False] * 1000000
queue = deque()

loop_start_point = dfs(a, p)
# print(queue)
result = 0

while queue:
    cur_data = queue.popleft()
    if cur_data == loop_start_point:
        break
    result += 1
    # print(result)

if result != 0:
    result += 1
print(result)

# import sys
# a, p = map(int, sys.stdin.readline().split())
# seq = [a]
# while True:
#     t = seq[-1]
#     val = 0
#     while t:
#         val += ((t%10) ** p)
#         t //= 10
#     if val in seq:
#         sys.stdout.write(str(seq.index(val)))
#         break
#     else:
#         seq.append(val)


# 참고 https://haesoo9410.tistory.com/189