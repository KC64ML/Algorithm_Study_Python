import sys

read = sys.stdin.readline

while True:
    # input
    N, A, B = map(int, read().split())
    if N == 0:
        break

    q = []
    # 거리 계산
    for i in range(N):
        k, d1, d2 = map(int, read().split())
        q.append((abs(d1 - d2), k, d1, d2))

    q.sort()
    result = 0
    while q:
        dumb, k, d1, d2 = q.pop()

        if d1 <= d2:
            if k <= A:
                A -= k
                result += k * d1
            else:
                result += A * d1
                left = (k - A)
                A = 0
                result += left * d2
                B -= left
        else:
            if k <= B:
                B -= k
                result += k * d2
            else:
                result += B * d2
                left = (k - B)
                B = 0
                result += left * d1
                A -= left
    print(result)
