import sys

read = sys.stdin.readline

t = int(read())


def verify(start, end):
    if start >= end:
        return True

    left = start
    right = end

    # 이분 탐색
    while left < right:

        if paper[left] == paper[right]:
            return False

        left += 1
        right -= 1

    return verify(start, right - 1)


for _ in range(t):
    paper = list(map(int, read().rstrip()))

    if verify(0, len(paper) - 1):
        print("YES")
    else:
        print("NO")
