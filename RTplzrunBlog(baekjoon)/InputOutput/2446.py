n = int(input())

cnt_idx = 0

for idx in range(n, 0, -1):
    print(" " * cnt_idx + "*" * (2 * idx - 1))
    cnt_idx += 1
cnt_idx -= 1
for idx in range(2, n + 1):
    cnt_idx -= 1
    print(" " * cnt_idx + "*" * (2 * idx - 1))
