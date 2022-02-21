from sys import stdin as s

t = int(s.readline())

cnt = 0

def dfs(start, visited, arr):
    if visited[start]:
        return -1

    print(start, end=" ")
    visited[start] = True
    dfs(arr[start], visited, arr)

    return 1


for _ in range(t):
    n = int(s.readline())
    arr = list(map(int, s.readline().split()))
    arr = [0] + arr
    print(arr)
    visited = [False] * (len(arr) + 1)
    result = 0

    for i in range(len(arr)):
        if i == arr[i]:
            continue

        if visited[i]:
            continue

        print("체크 ", i)
        cnt = i
        if dfs(i, visited, arr) == -1:
            result += 1
        print(visited)
        print()
    print(visited)
    print(result)

