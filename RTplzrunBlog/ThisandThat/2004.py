from sys import stdin as s

n, m = map(int, s.readline().split())


def comb(cur_data, div):
    cnt = 0
    while cur_data:
        cur_data //= div
        cnt += cur_data

    return cnt


two_data = comb(n, 2) - comb(m, 2) - comb((n - m), 2)
five_data = comb(n, 5) - comb(m, 5) - comb((n - m), 5)

print(min(two_data, five_data))
