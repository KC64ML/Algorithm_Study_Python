import sys

read = sys.stdin.readline

n, m, k = map(int, read().split())

position = list(map(int, read().split()))


def solution():
    # 이분 탐색을 해야 한다.
    # 매 순간 나오는 결과를 저장한다.
    res = 0
    start = 0
    end = n

    while start <= end:
        mid = (start + end) // 2

        pes = 0
        referee = 1
        curRes = '1'

        # 중앙 값을 기준으로 찾는다.
        for i in range(1, k):
            if position[i] - position[pes] >= mid:
                referee += 1
                pes = i
                curRes += '1'

                # 심판 다 구함
                if referee == m:
                    break
            else:
                curRes += '0'

        while len(curRes) < k:
            curRes += '0'

        if referee == m:
            start = mid + 1
            res = curRes
        else:
            end = mid - 1

    print(res)

solution()