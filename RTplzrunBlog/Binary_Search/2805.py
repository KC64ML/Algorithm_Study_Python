import sys

read = sys.stdin.readline

n, m = map(int, read().split())

arr = list(map(int, read().split()))

start, end = 1, max(arr)  # 이분 탐색 검색 범위 설정

while start <= end:
    # print("start, end : ", start, end, end=" ")
    mid = (start + end) // 2
    find_m = 0

    for i in arr:
        if i > mid:
            find_m += (i - mid)


    # 발목 높이 m보다 크거나 같다면 start를 늘린다.
    # 발목 높이 m보다 작다면 end를 줄인다.

    if find_m >= m:
        start = mid + 1
    else:
        end = mid - 1

    # print("mid : ",mid)

print(end)


