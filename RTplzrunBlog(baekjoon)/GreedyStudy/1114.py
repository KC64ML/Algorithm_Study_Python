import sys

read = sys.stdin.readline

L, K, C = map(int, read().split())
cuts = [0, L] + list(map(int, read().split()))
cuts.sort()


def solution(x):
    cnt = 0
    cut_start = L
    prev = []
    first = 0

    # x라는 길이를 넘으면 자른다.
    for i in range(len(cuts) - 1, -1, -1):
        diff = cuts[i] - cuts[i - 1]
        total = cut_start - cuts[i]
        print("i : ", i, " cur_start", cut_start, "cuts : ", cuts, "total : ", total, " x: ", x, " diff : ", diff)
        if diff > x:
            # 이분탐색, 오른쪽
            return 10001, 0
        elif total > x:
            # i번째 자르고, i+1을 저장
            cut_start = cuts[i + 1]
            prev.append(cuts[i + 1])
            cnt += 1
        else:
            continue

    if cnt < C:
        first = cuts[1]
    else:
        # 인덱스 뒤에서부터 삽입되니, 마지막으로 추가된 것이 first 값이 된다.
        first = prev[-1]

    return cnt, first


lo = 0
hi = L
answer = 0
first_cut = 0
while lo <= hi:
    mid = (lo + hi) // 2

    cnt, first = solution(mid)

    if C < cnt:
        lo = mid + 1
    else:
        answer = mid
        first_cut = first
        hi = mid - 1

print(answer, first_cut)