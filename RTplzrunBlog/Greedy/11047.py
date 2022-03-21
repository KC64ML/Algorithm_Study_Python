import sys

read = sys.stdin.readline

n, k = map(int, read().split())

greedy = []


for idx in range(n):
    s = int(read())

    # 위치 저장
    if s <= k:
        greedy.append(s)


cnt = 0

# print(coin_max_line)

for idx in range(len(greedy) - 1, -1, -1):
    cnt += k // greedy[idx]
    k %= greedy[idx]

    # print()
    # print("idx : ", idx , " cnt : ", cnt, "k : ", k, "greedy[idx]",greedy[idx])

    if k == 0:
        break


print(cnt)





